# Image Prompt

**Creative ID:** a4-f9-2026-03-12
**Format:** F9 — Bold Typography / Magazine Cover
**Aspect Ratios:** 1:1 and 9:16

## Visual Concept

Solid dark premium background (deep navy or near-black with a very subtle warm gradient). The typography IS the design — filling 75% of the image space. Large bold white headline at top. Medium white body text in the middle listing the ROI math. Bold gold price anchor at bottom. Magazine cover / high-end brand editorial feel. Minimal visual texture. No scene photography — text and color only.

## Fal.ai API Request — 1:1 (Square Feed)

```json
{
  "prompt": "Facebook ad creative, square 1:1 format. Bold typography magazine cover style. Background: solid deep dark navy (#0A0E2A) with extremely subtle warm radial gradient glow at center, nearly imperceptible. No photography. The entire design is typography. Text rendered in the image -- top 25 percent: 'STOP BUYING' in massive ultra-heavy white sans-serif font (similar to Impact or Helvetica Black Ultra), all-caps, filling full width with generous side padding. Text rendered in the image -- upper middle: '$10,000 MACHINES' in the same massive ultra-heavy font but in warm gold color (#D4A853), all-caps, same scale. Text rendered in the image -- center: a thin warm gold horizontal rule line spanning 60 percent of width. Text rendered in the image -- center-lower: 'Zero overhead. $180 per session.' in large bold white sans-serif, centered. Text rendered in the image -- lower: '$67 gets your team certified in ONE weekend.' in medium bold white sans-serif, centered. Text rendered in the image -- bottom area: 'Zero Machines. $180/Session. Pure ROI.' in large heavy-weight white sans-serif (slightly smaller than the top headline but still prominent), centered. Ultra-premium magazine editorial look. Commercial ad quality. No watermarks. No photography. Output optimized for Facebook Ads.",
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
  "prompt": "Facebook Stories ad creative, vertical 9:16 format. Bold typography magazine cover style. Background: solid deep dark navy (#0A0E2A) with extremely subtle warm radial gradient glow at center. No photography. Pure typography design. Text rendered in the image -- top area: 'STOP BUYING' in massive ultra-heavy white sans-serif font (Impact or Helvetica Black Ultra style), all-caps, large and commanding. Below it: '$10,000 MACHINES' in the same massive font in warm gold (#D4A853), all-caps. Text rendered in the image -- center area: thin warm gold horizontal rule. Then: 'Zero overhead. $180 per session.' in large bold white sans-serif, centered. Below: '$67 gets your team certified in ONE weekend.' in medium bold white sans-serif, centered. Text rendered at the bottom area: 'Zero Machines. $180/Session. Pure ROI.' in large heavy-weight white sans-serif. Very generous line spacing. Ultra-premium magazine editorial look. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
  "aspect_ratio": "9:16",
  "num_images": 1,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```
