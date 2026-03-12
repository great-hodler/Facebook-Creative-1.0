# Face Sculptor Academy — Facebook Ads Creative System

AI-powered creative production department for Face Sculptor Academy Facebook Ads.
Produces static creatives (image + copy + headline) ready for upload to Facebook Ads Manager.

**Product:** Online face massage course for beauty professionals (masseurs, estheticians, cosmetologists).
**Market:** English-speaking.
**Website:** https://facesculptor-academy.online

---

## Stack

- **Claude claude-opus-4-6** via Claude Code slash commands (`/batch`, `/marketer`, `/copywriter`, `/art-director`)
- **Fal.ai API** — `fal-ai/nano-banana-pro` (Gemini 3 Pro Image) for complete creative generation
- **Markdown** — all knowledge, prompts, and output files
- **`.env`** — API key storage (gitignored, never committed)

---

## Key Folders

| Folder | Purpose |
|--------|---------|
| `knowledge-base/` | Product description, audience research, copy rules, hooks, examples |
| `strategy/` | 8 angles, 9 formats, production grid (creative tracker) |
| `.claude/commands/` | Slash command agent prompts (`/batch`, `/marketer`, `/copywriter`, `/art-director`) |
| `templates/` | Creative brief and output templates |
| `workflows/` | Production guide and quality checklist |
| `output/` | One folder per produced creative + batch summary files |
| `learnings/` | Weekly performance notes (feeds back into agent prompts) |
| `plan/` | Strategy document |

---

## How to Produce Creatives

### Batch Mode (Primary — Fully Autonomous)

```
/batch
```

That's it. Claude reads all knowledge files, auto-selects 10 diverse angle/format/persona combos based on the priority matrix, runs the full Marketer → Copywriter → Art Director pipeline for each, calls the Fal.ai API, downloads images, and saves everything. No human input required mid-run.

**Output per batch:** 10 creative folders + 1 batch summary file. ~20 images (1:1 + 9:16 per creative). Cost: ~$3.00.

### Manual Mode (For Exploration or Single Creatives)

1. Open `strategy/creative-grid.md` → select angle + format + persona combo
2. Run `/marketer` → provide Angle ID + Persona ID → get `brief.md`
3. Run `/copywriter` → review Copy A and Copy B → select version and headline
4. Run `/art-director` → provide Format ID + approved copy → get `image-prompt.md`
5. API call is automatic within the command, or paste JSON to Fal.ai playground manually

---

## API Key

Stored in `.env` at project root:
```
FAL_KEY=your-key-here
```

The `.env` file is gitignored. Never hardcode the key in any markdown or commit it.

---

## Rules

- All files in **English only** — no exceptions
- Do not invent performance data — use only what is in `learnings/` folder
- Output images must be **complete creatives**: text, visuals, layout rendered by Nano Banana Pro
- Each creative lives in its own output folder: `output/[a1]-[f8]-[2026-03-12]/`
- **Batch mode output files per creative:** `brief.md`, `copy-final.md`, `image-prompt.md`, `image-1x1-final.png`, `image-9x16-final.png`, `approved.md`
- **Manual mode output files per creative:** `brief.md`, `copy-a.md`, `copy-b.md`, `image-prompt.md`, `image-1x1-final.png`, `image-9x16-final.png`, `approved.md`
- Primary aspect ratios: **1:1** (square feed) and **9:16** (stories) — both generated per creative
- `num_images: 1` in all Fal.ai API calls — the model generates one image per call
- Images (`.png`) are gitignored — not committed to repo
- `/batch` runs fully autonomously — never ask for human approval mid-pipeline
