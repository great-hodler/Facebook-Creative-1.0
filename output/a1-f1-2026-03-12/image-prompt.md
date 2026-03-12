# Image Prompt

**Creative ID:** a1-f1-2026-03-12
**Format:** F1 — Demographic Call-Out
**Aspect Ratios:** 1:1 and 9:16

## Visual Concept

Top 40% of the image: solid dark navy block containing the bold demographic call-out headline in large white all-caps text. Bottom 60%: warm, aspirational photo of a professional esthetician at work — close-up of skilled hands on a client's face in a premium spa setting, golden light. The contrast between the commanding dark text block above and the warm inviting scene below creates a scroll-stopping pattern interrupt. The viewer reads the call-out, then sees themselves in the scene.

## Fal.ai API Request — 1:1 (Square Feed)

```json
{
  "prompt": "Facebook ad creative, square 1:1 format. Demographic call-out style. Top 40 percent of image: solid dark navy (#0A0E2A) rectangle spanning full width. Text rendered in the image -- inside the dark top block, centered: 'ATTENTION ESTHETICIANS:' in massive ultra-heavy white sans-serif font (Impact or Helvetica Black Ultra style), all-caps, filling the full width with generous side padding, very large. Below it on the same dark block in slightly smaller bold white sans-serif: 'Your hands can make $180 per session in 45 min.' centered. Bottom 60 percent of image: warm photorealistic scene. Close-up of a professional esthetician's skilled hands performing precise anatomical jaw-lifting technique on a reclined client. Client's face is radiant, sculpted, relaxed. Warm golden-amber spa lighting. Premium white treatment bed, clean luxury spa background. Soft bokeh. The scene is aspirational — this is the income and lifestyle being offered. Text rendered in the image -- bottom strip (bottom 8 percent): thin solid dark navy strip. Inside: 'Estheticians: Charge $180 in 45 Minutes.' in bold white sans-serif, centered. Photorealistic. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
  "aspect_ratio": "1:1",
  "num_images": 1,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```

## Fal.ai API Request — 9:16 (Stories / Reels)

```json
{
  "prompt": "Facebook Stories ad creative, vertical 9:16 format. Demographic call-out style. Top 35 percent of image: solid dark navy (#0A0E2A) rectangle spanning full width. Text rendered in the image -- inside the dark top block: 'ATTENTION ESTHETICIANS:' in massive ultra-heavy white sans-serif (Impact or Helvetica Black Ultra), all-caps, very large and commanding. Below it in slightly smaller bold white sans-serif: 'Your hands can make $180 per session in 45 min.' centered. Bottom 65 percent of image: warm photorealistic scene. Close-up of professional esthetician's skilled hands performing precise jaw-lifting technique on a radiant client. Warm golden-amber spa lighting. Premium spa setting, white treatment bed, soft bokeh background. Text rendered in the image -- bottom strip: thin dark navy strip. Inside: 'Estheticians: Charge $180 in 45 Minutes.' in bold white sans-serif, centered. Photorealistic. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
  "aspect_ratio": "9:16",
  "num_images": 1,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```
