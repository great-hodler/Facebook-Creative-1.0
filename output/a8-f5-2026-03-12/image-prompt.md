# Image Prompt

**Creative ID:** a8-f5-2026-03-12
**Format:** F5 — Split-Screen Comparison
**Aspect Ratios:** 1:1 and 9:16

## Visual Concept

Clean 50/50 vertical split. LEFT HALF (cool, desaturated): a lash artist hunched over a client, face close to the client's eyes, magnifying lamp visible, body curled and tense. Expression suggests strain and fatigue. Label chip: "3-HOUR LASH SET". RIGHT HALF (warm golden): a practitioner standing upright and relaxed, hands working confidently on a client's jawline, client's face visibly sculpted. Warm golden spa lighting. Practitioner's posture is open, comfortable, professional. Label chip: "OSTEO-LIFT · 45 MIN". Thin white dividing line. Top dark band: "Your Back Deserves Better." Bottom dark band: "$180 in 45 Min. Your Back Will Thank You."

## Fal.ai API Request — 1:1 (Square Feed)

```json
{
  "prompt": "Facebook ad creative, square 1:1 format. Clean professional split-screen with thin white vertical dividing line at exact center. LEFT HALF: slightly desaturated cool blue-gray color grade. Female lash artist bent over a client, magnifying lamp in background, body hunched forward at awkward angle, face very close to client's closed eyes, tense posture suggesting back strain and eye fatigue. Flat cool studio lighting. RIGHT HALF: warm golden-amber lighting. Female practitioner standing upright and relaxed with excellent posture, both hands working confidently on a reclined client's sculpted jawline, client face visibly lifted and defined. Clean luxury spa background, warm ivory and gold tones. Text rendered in the image -- upper-left area, small rounded dark charcoal chip: '3-HOUR LASH SET' in small white all-caps sans-serif. Text rendered in the image -- upper-right area, small rounded dark chip: 'OSTEO-LIFT 45 MIN' in small warm gold (#D4A853) all-caps sans-serif. Text rendered in the image -- top full-width band (top 12 percent): solid dark navy (#0A0E2A) strip. Inside: 'Your Back Deserves Better.' in bold white sans-serif, centered. Text rendered in the image -- bottom full-width band (bottom 12 percent): solid dark navy (#0A0E2A) strip. Inside: '$180 in 45 Min. Your Back Will Thank You.' in large heavy-weight white sans-serif (Helvetica Black style), centered. Photorealistic. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
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
  "prompt": "Facebook Stories ad creative, vertical 9:16 format. Clean professional split-screen occupying the middle 70 percent of the image. Thin white vertical dividing line at exact horizontal center. LEFT HALF: desaturated cool blue-gray. Lash artist hunched over client, magnifying lamp visible, body tense and curled, back strain evident. RIGHT HALF: warm golden-amber lighting. Practitioner standing upright, relaxed posture, confident hands on client's jawline, sculpted face, luxury spa. Text rendered in the image -- top band (top 15 percent): solid dark navy (#0A0E2A) strip full width. Inside: 'Your Back Deserves Better.' in bold white sans-serif, centered. Text rendered in the image -- upper-left split label chip: '3-HOUR LASH SET' in white all-caps. Text rendered in the image -- upper-right split label chip: 'OSTEO-LIFT 45 MIN' in warm gold all-caps. Text rendered in the image -- bottom band (bottom 15 percent): solid dark navy (#0A0E2A) strip full width. Inside: '$180 in 45 Min. Your Back Will Thank You.' in large heavy-weight white sans-serif, centered. Photorealistic. Commercial ad quality. No watermarks. Output optimized for Facebook Ads.",
  "aspect_ratio": "9:16",
  "num_images": 1,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```
