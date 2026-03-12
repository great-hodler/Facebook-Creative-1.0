# Image Prompt

**Creative ID:** a2-f5-2026-03-12
**Format:** F5 — Split-Screen Comparison
**Aspect Ratios:** 1:1 and 9:16

## Visual Concept

Clean 50/50 vertical split. LEFT HALF (cool, muted): a beauty practitioner applying standard facial cream to a client, client expression pleasant but unremarkable, slight blur of product bottles in background. Label chip at top-left: "STANDARD FACIAL". RIGHT HALF (warm golden): close-up of skilled hands performing deep anatomical jawline work on a client, client's face visibly defined and lifted, premium spa setting, warm golden light. Label chip at top-right: "OSTEO-LIFT". Thin white dividing line at center. Top full-width dark navy band: "The Secret Top 1% Beauty Pros Use for Jaw-Dropping Results in 45 Min." Bottom full-width dark navy band: "Deliver Results That Last 3–6 Months."

## Fal.ai API Request — 1:1 (Square Feed)

```json
{
  "prompt": "Facebook ad creative, square 1:1 format. Clean professional split-screen with thin white vertical dividing line at exact center. LEFT HALF: slightly desaturated cool blue-gray color grade. Beauty practitioner applying facial cream to a client lying on treatment bed. Client expression pleasant but neutral, no visible wow factor. Product bottles visible on tray. Flat cool professional lighting. RIGHT HALF: warm golden-amber lighting. Close-up of skilled professional hands performing precise deep anatomical jawline lifting technique on a radiant client. Client face visibly sculpted and defined. Clean luxury spa background, warm ivory and gold tones. Text rendered in the image -- upper-left area, small rounded dark charcoal chip: 'STANDARD FACIAL' in small white all-caps sans-serif. Text rendered in the image -- upper-right area, small rounded dark chip: 'OSTEO-LIFT' in small warm gold (#D4A853) all-caps sans-serif. Text rendered in the image -- top full-width band (top 12 percent): solid dark navy (#0A0E2A) strip. Inside: 'The Secret Top 1% Beauty Pros Use for Jaw-Dropping Results in 45 Min.' in bold white sans-serif, centered. Text rendered in the image -- bottom full-width band (bottom 12 percent): solid dark navy (#0A0E2A) strip. Inside: 'Deliver Results That Last 3-6 Months.' in large heavy-weight white sans-serif (Helvetica Black style), centered. Photorealistic. Commercial ad quality. No watermarks. No stock photo cliches. Output optimized for Facebook Ads.",
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
  "prompt": "Facebook Stories ad creative, vertical 9:16 format. Clean professional split-screen occupying the middle 70 percent of the image. Thin white vertical dividing line at exact horizontal center. LEFT HALF: slightly desaturated cool blue-gray. Beauty practitioner applying facial cream to client, neutral expression, product bottles visible. RIGHT HALF: warm golden-amber lighting. Skilled professional hands doing deep anatomical jawline work on radiant sculpted client. Luxury spa background. Text rendered in the image -- top band (top 15 percent): solid dark navy (#0A0E2A) strip full width. Inside: 'The Secret Top 1% Beauty Pros Use for Jaw-Dropping Results in 45 Min.' in bold white sans-serif, centered. Text rendered in the image -- upper-left split label chip: 'STANDARD FACIAL' in white all-caps. Text rendered in the image -- upper-right split label chip: 'OSTEO-LIFT' in warm gold all-caps. Text rendered in the image -- bottom band (bottom 15 percent): solid dark navy (#0A0E2A) strip full width. Inside: 'Deliver Results That Last 3-6 Months.' in large heavy-weight white sans-serif, centered. Photorealistic. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
  "aspect_ratio": "9:16",
  "num_images": 1,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```
