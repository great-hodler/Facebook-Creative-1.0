# Face Sculptor Academy — Facebook Ads Creative System

AI-powered creative production department for Face Sculptor Academy Facebook Ads.
Produces static creatives (image + copy + headline) ready for upload to Facebook Ads Manager.

**Product:** Online face massage course for beauty professionals (masseurs, estheticians, cosmetologists).
**Market:** English-speaking.
**Website:** https://facesculptor-academy.online

---

## Stack

- **Claude claude-opus-4-6** via Claude Code slash commands (`/marketer`, `/copywriter`, `/art-director`)
- **Fal.ai API** — `fal-ai/nano-banana-pro` (Gemini 3 Pro Image) for complete creative generation
- **Markdown** — all knowledge, prompts, and output files

---

## Key Folders

| Folder | Purpose |
|--------|---------|
| `knowledge-base/` | Product description, audience research, copy rules, hooks, examples |
| `strategy/` | 8 angles, 9 formats, production grid (creative tracker) |
| `.claude/commands/` | Slash command agent prompts (`/marketer`, `/copywriter`, `/art-director`) |
| `templates/` | Creative brief and output templates |
| `workflows/` | Production guide and quality checklist |
| `output/` | One folder per produced creative |
| `learnings/` | Weekly performance notes (feeds back into agent prompts) |
| `plan/` | Strategy document |

---

## How to Produce a Creative

1. Open `strategy/creative-grid.md` → check the box for angle + format + persona combo
2. Run `/marketer` → provide Angle ID + Persona ID → review and approve `brief.md`
3. Run `/copywriter` → review Copy A and Copy B → select preferred version and headline
4. Run `/art-director` → provide Format ID + approved copy → review `image-prompt.md`
5. Submit the JSON from `image-prompt.md` to Fal.ai API (endpoint: `fal-ai/nano-banana-pro`)
6. Review generated images against `workflows/quality-checklist.md`
7. Save final image as `image-final.png` in the output folder → ready for upload

---

## Rules

- All files in **English only** — no exceptions
- No code files — this is a content and prompt system
- Do not invent performance data — use only what is in `learnings/` folder
- Output images must be **complete creatives**: text, visuals, layout rendered by Nano Banana Pro
- Each creative lives in its own output folder: `output/[a1]-[f8]-[2025-07-01]/`
- Required output files per creative: `brief.md`, `copy-a.md`, `copy-b.md`, `image-prompt.md`, `image-final.png`, `approved.md`
- Primary aspect ratios: **1:1** (square) and **9:16** (stories). Optional: **4:5** (feed vertical)
