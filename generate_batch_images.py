#!/usr/bin/env python3
"""
generate_batch_images.py
Reads image-prompt.json from each output/* folder and calls the kie.ai API
(Nano Banana Pro / Gemini 3 Pro Image) to generate images.
Saves image-1x1-final.jpg and image-9x16-final.jpg in each creative folder.

Usage:
    python3 generate_batch_images.py

Requirements:
    pip install requests
"""

import json
import os
import time
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library not installed. Run: pip install requests")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

KIE_CREATE_URL = "https://api.kie.ai/api/v1/jobs/createTask"
KIE_POLL_URL   = "https://api.kie.ai/api/v1/jobs/recordInfo"
KIE_MODEL      = "nano-banana-pro"

MAX_RETRIES    = 3
RETRY_DELAYS   = [3, 6, 12]   # seconds between retries on create
POLL_INTERVAL  = 5             # seconds between poll attempts
POLL_TIMEOUT   = 180           # seconds max wait per image

# ── Load API key ──────────────────────────────────────────────────────────────

def load_kie_key():
    env_path = Path(".env")
    if not env_path.exists():
        print("ERROR: .env file not found in current directory.")
        print("Create .env with: KIE_API_KEY=your_key_here")
        sys.exit(1)

    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("KIE_API_KEY="):
                key = line.split("=", 1)[1].strip()
                if key:
                    return key

    print("ERROR: KIE_API_KEY not found in .env file.")
    sys.exit(1)

# ── Create task ───────────────────────────────────────────────────────────────

def create_task(kie_key, prompt, aspect_ratio):
    """POST to kie.ai createTask. Returns taskId string or None on failure."""
    headers = {
        "Authorization": f"Bearer {kie_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": KIE_MODEL,
        "input": {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "output_format": "jpg"
        }
    }

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.post(KIE_CREATE_URL, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            if data.get("code") == 200 and data.get("data", {}).get("taskId"):
                return data["data"]["taskId"]
            raise ValueError(f"Unexpected response: {data}")
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAYS[attempt]
                print(f"    create attempt {attempt+1} failed: {e} — retrying in {delay}s")
                time.sleep(delay)
            else:
                print(f"    create FAILED after {MAX_RETRIES} attempts: {e}")
                return None

# ── Poll task ─────────────────────────────────────────────────────────────────

def poll_task(kie_key, task_id):
    """Poll recordInfo until success or fail. Returns image URL or None."""
    headers = {"Authorization": f"Bearer {kie_key}"}
    deadline = time.time() + POLL_TIMEOUT

    while time.time() < deadline:
        try:
            resp = requests.get(
                KIE_POLL_URL,
                headers=headers,
                params={"taskId": task_id},
                timeout=30
            )
            resp.raise_for_status()
            data = resp.json()
            task = data.get("data", {})
            state = task.get("state", "")

            if state == "success":
                result_json = task.get("resultJson", "{}")
                result = json.loads(result_json)
                urls = result.get("resultUrls", [])
                if urls:
                    return urls[0]
                raise ValueError("No resultUrls in resultJson")

            if state == "fail":
                print(f"    task failed: {task.get('failMsg', 'unknown error')}")
                return None

            # still waiting/queuing/generating — keep polling
            print(f"    [{state}] ...", end=" ", flush=True)
            time.sleep(POLL_INTERVAL)

        except Exception as e:
            print(f"    poll error: {e}")
            time.sleep(POLL_INTERVAL)

    print(f"    TIMEOUT after {POLL_TIMEOUT}s")
    return None

# ── Download image ────────────────────────────────────────────────────────────

def download_image(url, output_path):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    kie_key = load_kie_key()
    print("KIE_API_KEY loaded ✓")

    output_dir = Path("output")
    if not output_dir.exists():
        print("ERROR: 'output' directory not found.")
        sys.exit(1)

    prompt_files = sorted(output_dir.glob("*/image-prompt.json"))

    if not prompt_files:
        print("No image-prompt.json files found in output/ subfolders.")
        sys.exit(0)

    print(f"\nFound {len(prompt_files)} creative(s) with image-prompt.json\n")
    print("─" * 60)

    stats = {"success": 0, "skipped": 0, "failed": 0}

    for prompt_file in prompt_files:
        folder = prompt_file.parent
        creative_id = folder.name

        with open(prompt_file) as f:
            data = json.load(f)

        print(f"\n▶ {creative_id}")

        for ratio_key, suffix in [("prompt_1x1", "1x1"), ("prompt_9x16", "9x16")]:
            out_path = folder / f"image-{suffix}-final.jpg"

            if out_path.exists():
                print(f"  ↳ {suffix} already exists, skipping")
                stats["skipped"] += 1
                continue

            prompt_block = data.get(ratio_key)
            if not prompt_block:
                print(f"  ✗ {suffix} prompt missing in image-prompt.json")
                stats["failed"] += 1
                continue

            prompt_text  = prompt_block.get("prompt", "")
            aspect_ratio = prompt_block.get("aspect_ratio", ratio_key.split("_")[1].replace("x", ":"))

            print(f"  ↳ {suffix}: creating task ...", end=" ", flush=True)
            task_id = create_task(kie_key, prompt_text, aspect_ratio)
            if not task_id:
                stats["failed"] += 1
                continue

            print(f"task {task_id[:12]}... polling", end=" ", flush=True)
            url = poll_task(kie_key, task_id)
            if not url:
                stats["failed"] += 1
                continue

            download_image(url, out_path)
            size_kb = out_path.stat().st_size // 1024
            print(f"✓ saved ({size_kb} KB)")
            stats["success"] += 1

    print("\n" + "─" * 60)
    print(f"Done. Generated: {stats['success']} | Skipped: {stats['skipped']} | Failed: {stats['failed']}")
    estimated_cost = stats["success"] * 0.02
    print(f"Estimated cost: ${estimated_cost:.2f}")

    if stats["failed"] > 0:
        print(f"\n⚠ {stats['failed']} image(s) failed. Re-run the script to retry — existing images are skipped.")


if __name__ == "__main__":
    main()
