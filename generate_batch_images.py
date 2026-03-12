#!/usr/bin/env python3
"""
generate_batch_images.py
Reads image-prompt.json from each output/* folder and calls the Fal.ai API
to generate images. Saves image-1x1-final.png and image-9x16-final.png in each folder.

Usage:
    python3 generate_batch_images.py

Requirements:
    pip install requests python-dotenv
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

FAL_API_URL = "https://fal.run/fal-ai/nano-banana-pro"
MAX_RETRIES = 3
RETRY_DELAYS = [3, 6, 12]  # seconds between retries

# ── Load API key ──────────────────────────────────────────────────────────────

def load_fal_key():
    env_path = Path(".env")
    if not env_path.exists():
        print("ERROR: .env file not found in current directory.")
        print("Create .env with: FAL_KEY=your_key_here")
        sys.exit(1)

    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("FAL_KEY="):
                key = line.split("=", 1)[1].strip()
                if key:
                    return key

    print("ERROR: FAL_KEY not found in .env file.")
    sys.exit(1)

# ── API call with retry ───────────────────────────────────────────────────────

def call_fal_api(fal_key, payload, creative_id, aspect_ratio):
    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.post(
                FAL_API_URL,
                headers=headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            data = response.json()

            if "images" not in data or not data["images"]:
                raise ValueError(f"No images in response: {data}")

            image_url = data["images"][0]["url"]
            return image_url

        except Exception as e:
            if attempt < MAX_RETRIES:
                delay = RETRY_DELAYS[attempt]
                print(f"  ⚠ {creative_id} [{aspect_ratio}] attempt {attempt+1} failed: {e}")
                print(f"    Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"  ✗ {creative_id} [{aspect_ratio}] FAILED after {MAX_RETRIES+1} attempts: {e}")
                return None

# ── Download image ────────────────────────────────────────────────────────────

def download_image(url, output_path):
    response = requests.get(url, timeout=120)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    fal_key = load_fal_key()
    print(f"FAL_KEY loaded ✓")

    output_dir = Path("output")
    if not output_dir.exists():
        print("ERROR: 'output' directory not found.")
        sys.exit(1)

    # Find all image-prompt.json files
    prompt_files = sorted(output_dir.glob("*/image-prompt.json"))

    if not prompt_files:
        print("No image-prompt.json files found in output/ subfolders.")
        print("Run /batch first to generate creative packages.")
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

        # Process 1:1
        out_1x1 = folder / "image-1x1-final.png"
        if out_1x1.exists():
            print(f"  ↳ 1:1 already exists, skipping")
            stats["skipped"] += 1
        else:
            payload_1x1 = data.get("prompt_1x1")
            if not payload_1x1:
                print(f"  ✗ 1:1 prompt missing in image-prompt.json")
                stats["failed"] += 1
            else:
                print(f"  ↳ Generating 1:1 ...", end=" ", flush=True)
                url = call_fal_api(fal_key, payload_1x1, creative_id, "1:1")
                if url:
                    download_image(url, out_1x1)
                    size_kb = out_1x1.stat().st_size // 1024
                    print(f"✓ saved ({size_kb} KB)")
                    stats["success"] += 1
                else:
                    stats["failed"] += 1

        # Process 9:16
        out_9x16 = folder / "image-9x16-final.png"
        if out_9x16.exists():
            print(f"  ↳ 9:16 already exists, skipping")
            stats["skipped"] += 1
        else:
            payload_9x16 = data.get("prompt_9x16")
            if not payload_9x16:
                print(f"  ✗ 9:16 prompt missing in image-prompt.json")
                stats["failed"] += 1
            else:
                print(f"  ↳ Generating 9:16 ...", end=" ", flush=True)
                url = call_fal_api(fal_key, payload_9x16, creative_id, "9:16")
                if url:
                    download_image(url, out_9x16)
                    size_kb = out_9x16.stat().st_size // 1024
                    print(f"✓ saved ({size_kb} KB)")
                    stats["success"] += 1
                else:
                    stats["failed"] += 1

    print("\n" + "─" * 60)
    print(f"Done. Generated: {stats['success']} | Skipped: {stats['skipped']} | Failed: {stats['failed']}")
    estimated_cost = stats["success"] * 0.15
    print(f"Estimated cost: ${estimated_cost:.2f}")

    if stats["failed"] > 0:
        print(f"\n⚠ {stats['failed']} image(s) failed. Re-run the script to retry — existing images are skipped automatically.")


if __name__ == "__main__":
    main()
