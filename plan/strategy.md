# Facebook Ads Creative System — Strategy

## What This System Does

A systematic AI-powered process for producing Facebook Ads creatives for Face Sculptor Academy.
Each creative = complete ready-to-upload image (text + visual rendered by Nano Banana Pro via Fal.ai) + ad copy + headlines.

Production is **on-demand**: human selects angle + format + persona from the grid, then runs 3 slash commands in sequence.

---

## Critical Self-Audit

### 1. Does this plan solve the problem?

**Yes.** It replaces ad-hoc prompting with a predictable, structured production flow:
- Angles, formats, and personas are pre-defined (not invented per session)
- Three specialized agents run in sequence, each with specific files to read and specific outputs to produce
- Nano Banana Pro renders text inside the image — the output is a complete creative, no Canva required

### 2. Is there a simpler solution?

For agent execution: yes. Agents are just `.md` files in `.claude/commands/`. No code, no infrastructure. The human types `/marketer`, `/copywriter`, `/art-director` in sequence in Claude Code.

For image generation: the Fal.ai API call is straightforward. Manual (paste JSON in playground) or automated via `FAL_KEY`. Both work.

### 3. Weak spots

**Text rendering:** Nano Banana Pro (Gemini 3 Pro Image) renders text accurately, but the Art Director prompt must explicitly describe each text element — position, font weight, color, background block. Never rely on implicit placement.

**No feedback loop by default:** When creatives run on Facebook, performance data stays in Ads Manager. Fix: log key metrics weekly in `learnings/[YYYY-WW].md`. Agent prompts reference this folder — quality compounds over time.

**Grid complexity:** 8 angles × 9 formats × 5 personas = 360 theoretical combos. Solution: use the grid as a checkbox tracker, work in batches of 5–10 at a time.

### 4. What happens at scale?

The `strategy/creative-grid.md` tracker shows at a glance: what's been tested, what's a winner, what gaps remain. The `learnings/` folder compounds quality as agent prompts are updated based on real data. After 3 months, the best-performing angle/format combos become clear.

---

## Production Workflow (On-Demand)

```
TRIGGER: Human wants to produce a creative

Step 1 — Select from grid
  Open strategy/creative-grid.md
  Mark: [x] A1 × F8 × P2 | Booking Notification | Burnt-Out Solo

Step 2 — /marketer
  Reads: product-description.md, audience-research.md, angles.md
  Input:  Angle ID (A1–A8) + Persona ID (P1–P5)
  Output: brief.md
  Human: review → approve or edit (5 min)

Step 3 — /copywriter
  Reads: brief.md, creative-rules.md, hooks-reference.md, ad-copy-examples.md, industry-reference.md
  Output: copy-a.md + copy-b.md (each with 2 headlines)
  Human: select preferred version + headline (5 min)

Step 4 — /art-director
  Reads: brief.md, approved copy + headline, formats.md, creative-rules.md
  Input:  Format ID (F1–F9) + approved copy + headline
  Output: image-prompt.md (Fal.ai JSON + visual concept)
  Human: review → approve or edit (5 min)

Step 5 — Image Generation (Fal.ai API)
  Endpoint: POST https://fal.run/fal-ai/nano-banana-pro
  Auth:     Authorization: Key $FAL_KEY
  Body:     JSON from image-prompt.md
  Result:   2 image variants (PNG)

Step 6 — Quality Check + Final Selection
  Run workflows/quality-checklist.md
  Select best image → save as image-final.png
  Update creative-grid.md (mark cell done ✓)
  Save approved.md with selections and notes
```

---

## Fal.ai API — Nano Banana Pro

**Endpoint:** `POST https://fal.run/fal-ai/nano-banana-pro`
**Auth:** `Authorization: Key $FAL_KEY`

**Request body:**
```json
{
  "prompt": "[complete scene + exact text to render]",
  "aspect_ratio": "1:1",
  "num_images": 2,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```

**Supported aspect ratios:** `1:1` (primary), `9:16` (primary), `4:5` (optional)

**Response:**
```json
{
  "images": [{ "url": "https://...", "file_name": "output.png" }]
}
```

**Cost:** $0.15/image × 2 variants = $0.30 per creative. 20 creatives/week = $6/week.

**Text rendering rule:** Always describe text explicitly:
```
Text rendered at the top of the image: "ATTENTION MASSAGE THERAPISTS:"
in large bold white sans-serif font on a solid dark navy background block.
```

---

## Architecture

```
Facebook-Creative-1.0/
│
├── CLAUDE.md                          ← Project overview
├── plan/strategy.md                   ← This file
│
├── knowledge-base/                    ← Updated monthly
│   ├── product-description.md
│   ├── audience-research.md
│   ├── creative-rules.md
│   ├── hooks-reference.md
│   ├── ad-copy-examples.md
│   └── industry-reference.md
│
├── strategy/                          ← Updated per sprint
│   ├── angles.md                      ← 8 master angles
│   ├── formats.md                     ← 9 visual formats
│   └── creative-grid.md               ← Production tracker
│
├── .claude/commands/                  ← Slash commands
│   ├── marketer.md                    ← /marketer
│   ├── copywriter.md                  ← /copywriter
│   └── art-director.md               ← /art-director
│
├── templates/
│   ├── creative-brief-template.md
│   └── creative-output-template.md
│
├── workflows/
│   ├── production-guide.md
│   └── quality-checklist.md
│
├── learnings/
│   └── [YYYY-WW].md                   ← Performance notes
│
└── output/
    └── [a1]-[f8]-[2025-07-01]/
        ├── brief.md
        ├── copy-a.md
        ├── copy-b.md
        ├── image-prompt.md
        ├── image-final.png
        └── approved.md
```

---

## Stack

| Tool | Role | Why |
|------|------|-----|
| Claude claude-opus-4-6 | All text generation | Best reasoning for nuanced marketing briefs |
| Claude Code slash commands | Agent execution | Zero-config; reads .md files natively |
| Fal.ai / Nano Banana Pro | Image generation | Gemini 3 Pro: strong text rendering, $0.15/image, commercial rights |
| Markdown | All files | AI-readable, human-readable, version-controllable |
| Git | Version control | Full history of creative production and prompt evolution |

---

## Angles — 8 Master Angles

| ID | Angle | Core Promise | Target Segment | Emotional Trigger |
|----|-------|-------------|----------------|-------------------|
| A1 | Get Fully Booked | Fill your calendar with premium clients | Under-booked solo estheticians & therapists | Ambition / Income Anxiety |
| A2 | Deliver Better Results | Visible, lasting outcomes without injections | Results-driven practitioners | Professional Pride |
| A3 | Stand Out as Expert | Become the go-to facial architect in your area | Experienced but undifferentiated pros | Status / Recognition |
| A4 | Upgrade Your Skills | Master a cutting-edge, hands-only technique | Growth-oriented pros & SPA Directors | Curiosity / FOMO |
| A5 | Client Transformation | Show what's possible for your clients' faces | Visual-results focused practitioners | Inspiration / Aspiration |
| A6 | Social Proof | Hear from beauty pros who leveled up | Skeptical / risk-averse practitioners | Trust / Safety |
| A7 | Urgency / Scarcity | The industry is shifting. Don't get left behind. | Decision-delayed prospects | Fear of Missing Out |
| A8 | Pain Point | Stop losing clients and ruining your health | Burnt-out, physically strained pros | Pain Relief / Hope |

---

## Formats — 9 Visual Formats

| ID | Format | Concept |
|----|--------|---------|
| F1 | Demographic Call-Out | Massive headline calling out audience; aesthetic image below |
| F2 | Stop / Start Command | High-contrast; forces mindset shift from old to new |
| F3 | Native Social UI | Mimics iMessage/IG Story — drops the ad shield |
| F4 | Process Checklist | Educational listicle with emoji bullets on process shot |
| F5 | Split-Screen Comparison | "Old Way" vs "New Way" — visual side-by-side |
| F6 | Direct Offer / Price Anchor | Bottom funnel — bold $67 price + urgency |
| F7 | Anatomical / Scientific | Authority via anatomy visuals and fascial science |
| F8 | Booking / Payment Notification | Financial desire trigger — fake Stripe/booking notification |
| F9 | Bold Typography / Magazine Cover | 80% text IS the design — provocative statement |

---

## Personas — 5 ICP Profiles

| ID | Persona | Core Pain | Core Desire |
|----|---------|-----------|-------------|
| P1 | Skill-Upgrader (Massage Therapists, Cosmetologists) | Stagnation; competitors stealing clients | $180+ anatomical lifting skill |
| P2 | Burnt-Out Solo Pro (Solo Estheticians, Beauty Therapists) | 10-12hr days, income ceiling | 4-day week, premium pricing, waitlist |
| P3 | Switcher (Lash Artists, PMU Artists) | Back pain, eyesight damage, low hourly rate | Ergonomic high-ticket 45-min service |
| P4 | Business Owner (Salon Owners, SPA Directors) | Low margins, expensive machines no ROI | Zero-overhead premium service |
| P5 | Fresh Graduate (Newly Licensed Pros) | Empty calendar, imposter syndrome | Bulletproof method, results from day 1 |

---

## Recommended First Batch (High-Signal Combos)

| Priority | Angle | Format | Persona | Why |
|----------|-------|--------|---------|-----|
| ★ | A1 Get Fully Booked | F8 Booking Notification | P2 Burnt-Out Solo | Income desire + aspiration trigger = strong |
| ★ | A8 Pain Point | F2 Stop/Start | P3 Switcher | Specific pain (back/eyes) + clear pivot = sharp |
| ★ | A2 Better Results | F5 Split-Screen | P1 Skill-Upgrader | Visual proof format matches proof-seeking mindset |
| ★ | A6 Social Proof | F4 Process Checklist | P5 Fresh Graduate | Trust-building for skeptical new grads |
| ★ | A4 Upgrade Skills | F9 Bold Typography | P4 Business Owner | Direct ROI message for decision-makers |

---

## What Is Not in Scope

- Automated Facebook upload (manual keeps human oversight)
- Video creatives (static only)
- Multi-language versions (English only)
- Carousel automation (each slide = separate image call following same flow)
