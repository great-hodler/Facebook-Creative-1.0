# Image Prompt

**Creative ID:** a8-f2-2026-03-12
**Format:** F2 — Stop / Start Command
**Aspect Ratios:** 1:1 and 9:16

## Visual Concept

Stark, high-contrast minimalist design. Nearly 80% of the image is solid dark charcoal/black background with subtle spa texture. Two bold text blocks dominate: TOP BLOCK in large white heavy-weight type reads "STOP ruining your back for $80/set." CENTER LINE: a thin gold horizontal divider. BOTTOM BLOCK in large gold/warm-yellow heavy-weight type reads "START making $180 in 45 min with your hands." Tiny supporting text beneath the bottom block in small white: "Your body can do the Osteo-Lift for 20 years." Extreme minimalism — no scene, just text power.

## Fal.ai API Request — 1:1 (Square Feed)

```json
{
  "prompt": "Facebook ad creative, square 1:1 format. Stark minimalist high-contrast design. Background: solid very dark charcoal (#1A1A1A) with extremely subtle spa stone texture, almost black. The image is 85 percent text and negative space. A thin gold horizontal line divides the image exactly in half. Text rendered in the image -- upper half: 'STOP ruining your back' in massive heavy-weight white bold sans-serif font (similar to Helvetica Black, font size taking up most of the upper area), left-aligned with generous padding. Directly below in slightly smaller but still large white bold text: 'for $80 per set.' Text rendered in the image -- lower half: 'START making $180' in massive heavy-weight warm gold (#D4A853) bold sans-serif font, same size as the STOP text. Directly below in slightly smaller gold bold text: 'in 45 min with your hands.' Text rendered at very bottom in small white sans-serif: 'Your body can do the Osteo-Lift for 20 years.' Ultra-minimalist. No photography. No decorative elements except the gold divider line. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
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
  "prompt": "Facebook Stories ad creative, vertical 9:16 format. Stark minimalist high-contrast design. Background: solid very dark charcoal (#1A1A1A) with extremely subtle spa stone texture, almost black. The image is 85 percent text and negative space. A thin gold horizontal line divides the image at the midpoint. Text rendered in the image -- upper section: 'STOP ruining your back' in massive heavy-weight white bold sans-serif font (similar to Helvetica Black), centered, large. Directly below: 'for $80 per set.' in slightly smaller white bold text, centered. Text rendered in the image -- lower section: 'START making $180' in massive heavy-weight warm gold (#D4A853) bold sans-serif font, centered, same scale as the STOP text. Directly below: 'in 45 min with your hands.' in slightly smaller gold bold text, centered. Text rendered at very bottom in small white sans-serif: 'Your body can do the Osteo-Lift for 20 years.' Ultra-minimalist. No photography. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
  "aspect_ratio": "9:16",
  "num_images": 1,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```
