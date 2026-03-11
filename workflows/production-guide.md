# Production Guide — On-Demand Creative Workflow

This guide walks through the full process of producing one Facebook Ad creative from start to finish.
Production is triggered on-demand — run it whenever you need new creatives.

---

## Pre-Flight Check

Before starting, confirm:
- [ ] You have a FAL_KEY for Fal.ai API (or access to fal.ai playground)
- [ ] The knowledge base files are up to date (`knowledge-base/` folder)
- [ ] You have Claude Code open in this project directory

---

## Step 1 — Select a Creative from the Grid (2 min)

Open `strategy/creative-grid.md`.

Find a combo that fits what you want to test. Use the **Recommended First Batch** section if you are just starting.

Mark your selection: `[x]`

**Tip:** Match the combo to your current campaign objective:
- Cold traffic → A1 (Get Fully Booked), A8 (Pain Point), A4 (Upgrade Skills)
- Warm traffic → A2 (Better Results), A5 (Client Transformation), A6 (Social Proof)
- Retargeting → A7 (Urgency/Scarcity), A6 (Social Proof), A1 (Get Fully Booked)

---

## Step 2 — Run /marketer (5–10 min)

In Claude Code, type:

```
/marketer
```

When prompted, provide:
- Angle ID (e.g., `A1`)
- Persona ID (e.g., `P2`)

Claude will read the knowledge base files and produce a `brief.md`.

**Your job:** Read the brief. Ask yourself:
- Does this speak to the right person?
- Is the core message sharp and specific?
- Is the proof element real and relevant?

Make edits directly in `brief.md` if needed. Approve when satisfied.

Create output folder: `output/[a1]-[f8]-[YYYY-MM-DD]/` and save `brief.md` there.

---

## Step 3 — Run /copywriter (5–10 min)

In Claude Code, type:

```
/copywriter
```

Claude will read `brief.md` and all reference files, then produce `copy-a.md` and `copy-b.md`.

**Your job:** Read both versions. For each, check:
- Does the short hook (≤125 chars) stop the scroll?
- Is Copy A conceptually different from Copy B (different hook type)?
- Do the headlines (≤40 chars each) make you want to click?

Select:
- Preferred version: A or B
- Preferred headline: A or B

Save both files in the output folder. Note your selections.

---

## Step 4 — Run /art-director (5–10 min)

In Claude Code, type:

```
/art-director
```

Provide:
- Format ID (e.g., `F8`)
- Approved copy version (paste the short hook + headline you selected)

Claude will produce `image-prompt.md` with:
- Visual concept description (read this — does the image make sense?)
- Two JSON blocks: one for 1:1, one for 9:16

**Your job:** Read the visual concept. Ask:
- Does the image match the angle and persona?
- Is the text placement clear and readable?
- Does it feel premium, not generic?

Edit the JSON prompt directly if needed. Save `image-prompt.md` in the output folder.

---

## Step 5 — Generate Image via Fal.ai (2–5 min)

### Option A — Manual (Fal.ai Playground)

1. Go to [fal.ai/models/fal-ai/nano-banana-pro](https://fal.ai/models/fal-ai/nano-banana-pro)
2. Paste the JSON prompt from `image-prompt.md`
3. Generate 2 variants
4. Download the best image as `image-final.png`

### Option B — API Call

```bash
curl -X POST https://fal.run/fal-ai/nano-banana-pro \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d @image-prompt-1x1.json
```

Response will contain image URLs. Download the selected image.

**Generate both aspect ratios:**
- 1:1 for Facebook/Instagram Feed
- 9:16 for Stories/Reels

Save the selected images as:
- `image-final-1x1.png`
- `image-final-9x16.png`

---

## Step 6 — Quality Check (5 min)

Open `workflows/quality-checklist.md`.

Run through all 14 points. If any point fails, decide:
- Minor issue → fix the prompt and regenerate
- Major issue → go back to Step 2 or 3 and revise the brief or copy

---

## Step 7 — Complete the Package (2 min)

Create `approved.md` in the output folder using the template from `templates/creative-output-template.md`.

Fill in:
- Selected copy version + headline
- Selected aspect ratio(s)
- Quality checklist result
- Upload notes (campaign, ad set)

Update `strategy/creative-grid.md`: change `[x]` to `[✓]` for the completed combo.

---

## Step 8 — Upload to Facebook Ads Manager

The creative is now ready. Upload:
- `image-final-1x1.png` or `image-final-9x16.png`
- Copy the Primary Text from your approved copy file
- Copy the Headline from your approved copy file

Use the URL: `https://facesculptor-academy.online`

---

## After the Creative Runs (Ongoing)

After 3–7 days of running, log performance in `learnings/`:

```
learnings/[YYYY-WW].md
```

Use this format:
```markdown
# Week [N] Learnings

## Winners
- [Creative ID] | CTR: X% | CPL: $X | Notes: [why it worked]

## Losers
- [Creative ID] | CTR: X% | CPL: $X | Notes: [why it failed]

## Insights for Next Batch
- [What to test next based on data]
- [What to stop testing]
- [Any angle/format combos to prioritize]
```

This file will be read by the agents in future sessions to improve output quality.

---

## Troubleshooting

**Text in image is wrong or unreadable:**
→ Regenerate with a clearer text description in the prompt. Add: "Text must be rendered accurately and legibly. No artistic distortion of the text."

**Image looks generic or stock-photo-like:**
→ Add to prompt: "Authentic, editorial photography style. NOT a stock photo. Real practitioner, real client, natural environment."

**Copy feels too generic:**
→ Return to brief.md and sharpen the persona specifics. The more specific the persona description, the more specific the copy.

**Headline too long:**
→ The hard limit is 40 characters including spaces. Count before submitting.
