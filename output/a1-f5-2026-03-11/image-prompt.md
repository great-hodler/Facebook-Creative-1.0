# Image Prompt

**Creative ID:** A1-F5-2026-03-11
**Format:** [F5] — Split-Screen Comparison
**Aspect Ratios to Generate:** 1:1 (Square Feed) and 9:16 (Stories / Reels) — generate each separately

---

## Visual Concept

Clean 50/50 vertical split-screen with a thin white dividing line at center. LEFT HALF: slightly desaturated, cool blue-gray color grading — a tired solo esthetician (female, professional uniform) applying basic cream products to a client on a treatment bed, cluttered skincare bottles visible on a tray beside her, flat cool overhead lighting, resigned expression. Small label chip at top-left: "$50 STANDARD FACIAL" in white caps on dark charcoal background. RIGHT HALF: warm golden-amber lighting — close-up of trained professional hands performing precise anatomical Osteo-Lift technique along a client's jawbone and cheekbones, no products or tools in sight, client's face radiant and sculpted, clean premium spa background. Small label chip at top-right: "$180 OSTEO-LIFT" in gold/warm-white caps on dark background. Full-width dark navy strip across the top (12% of height): bold white text reads "POV: You finally charge $180/session." Full-width solid dark navy strip across the bottom (12% of height): large heavy bold white sans-serif text reads "From $50 Facials to $180 Sessions".

---

## Fal.ai API Request — 1:1 (Square Feed)

```json
{
  "prompt": "Facebook ad creative, square format 1:1. Clean professional split-screen design with a thin white vertical dividing line at the exact center. LEFT HALF (50% of image): slightly desaturated, cool blue-gray color grade. A tired female solo esthetician in professional uniform applying basic cream products to a client lying on a treatment bed. Cluttered skincare product bottles on a tray visible beside her. Flat, slightly dim cool overhead lighting. Her expression is resigned and fatigued. RIGHT HALF (50% of image): warm golden-amber lighting. Extreme close-up of skilled professional hands only — no face visible — performing a precise anatomical facial lift technique along a client's jawbone and cheekbones. No products, no tools, bare hands only. The client's skin is visibly radiant and sculpted. Clean, minimal luxury spa background. Warm ivory and gold tones. Text rendered in the image — top full-width band (top 12% of image): solid dark navy (#0A0E2A) background strip spanning full width. Inside this strip: 'POV: You finally charge $180/session.' displayed in bold white sans-serif font (similar to Helvetica Neue Bold), centered, medium size. Text rendered in the image — upper-left quadrant, inside a small rounded dark charcoal (#1A1A1A) chip: '$50 STANDARD FACIAL' in small white all-caps sans-serif font. Text rendered in the image — upper-right quadrant, inside a small rounded dark charcoal (#1A1A1A) chip: '$180 OSTEO-LIFT' in small warm gold (#D4A853) all-caps sans-serif font. Text rendered in the image — bottom full-width band (bottom 12% of image): solid dark navy (#0A0E2A) background strip spanning full width. Inside this strip: 'From $50 Facials to $180 Sessions' displayed in large heavy-weight white sans-serif font (similar to Helvetica Black), centered. Premium commercial beauty brand aesthetic. Photorealistic. Commercial ad quality. No watermarks. No stock photo clichés. Output optimized for Facebook Ads.",
  "aspect_ratio": "1:1",
  "num_images": 2,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```

---

## Fal.ai API Request — 9:16 (Stories / Reels)

```json
{
  "prompt": "Facebook Stories / Instagram Reels ad creative, vertical format 9:16. Clean professional split-screen design with a thin white vertical dividing line at the exact horizontal center of the frame. The split-screen occupies the middle 70% of the image height. LEFT HALF of split (50% of image width): slightly desaturated, cool blue-gray color grade. A tired female solo esthetician in professional uniform applying basic cream products to a client lying on a treatment bed. Cluttered skincare product bottles on a tray visible beside her. Flat, slightly dim cool overhead lighting. Her expression is resigned and fatigued. RIGHT HALF of split (50% of image width): warm golden-amber lighting. Extreme close-up of skilled professional hands only — no face visible — performing a precise anatomical facial lift technique along a client's jawbone and cheekbones. No products, no tools, bare hands only. The client's skin is visibly radiant and sculpted. Clean, minimal luxury spa background. Warm ivory and gold tones. Text rendered in the image — top band (top 15% of image): solid dark navy (#0A0E2A) background strip spanning full width. Inside this strip: 'POV: You finally charge $180/session.' displayed in bold white sans-serif font (similar to Helvetica Neue Bold), centered. Text rendered in the image — upper-left area of split-screen, inside a small rounded dark charcoal (#1A1A1A) chip: '$50 STANDARD FACIAL' in small white all-caps sans-serif font. Text rendered in the image — upper-right area of split-screen, inside a small rounded dark charcoal (#1A1A1A) chip: '$180 OSTEO-LIFT' in small warm gold (#D4A853) all-caps sans-serif font. Text rendered in the image — bottom band (bottom 15% of image): solid dark navy (#0A0E2A) background strip spanning full width. Inside this strip: 'From $50 Facials to $180 Sessions' displayed in large heavy-weight white sans-serif font (similar to Helvetica Black), centered. Premium commercial beauty brand aesthetic. Photorealistic. Commercial ad quality. No watermarks. No stock photo clichés. Output optimized for Facebook Ads.",
  "aspect_ratio": "9:16",
  "num_images": 2,
  "output_format": "png",
  "resolution": "1K",
  "safety_tolerance": "4"
}
```

---

## Notes for Human

1. **Text zone priority:** The top and bottom dark navy bands are the most critical elements — if the AI skips or misplaces either text, regenerate. The split-screen scene itself can have variation.

2. **Left vs. Right contrast:** The cold/desaturated left and warm/golden right must be clearly distinct at a glance (the "1-second rule"). If both sides render with similar lighting, adjust the prompt by adding: `"LEFT HALF: cold blue-toned color grading with desaturated muted palette"` and `"RIGHT HALF: warm golden-hour lighting with rich amber and ivory tones"`.

3. **Hands-only on the right:** The right side should show hands performing technique — NOT a full-body shot. If the AI renders a full practitioner on both sides, add: `"RIGHT HALF: tight close-up crop showing only the practitioner's hands on the client's jaw, no full body visible"`.

4. **Gold label chip:** The "$180 OSTEO-LIFT" label should render in warm gold (#D4A853), not white, to visually differentiate it from the "$50" label and reinforce premium value. If both labels render white, add: `"The right-side label chip uses gold-colored text to contrast with the white left-side label"`.

5. **Regeneration tip:** Run 2 variants per aspect ratio (num_images: 2). Select the variant where text is most legible and the visual contrast between the two halves is strongest.
