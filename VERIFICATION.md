# Verification, October 9, 2026 crew-photo refinement

Ready for local review at http://127.0.0.1:4173/.

- The hero now uses the original utility-piping crew photo. Its crop centers on the people, with object-position 50% 60%. The photo is eager-loaded and has descriptive alt text. The full desktop viewport layout and circular down link remain.
- Desktop at 1280 × 900: hero ends at 900.69px and there is no horizontal overflow. The normal browser panel view and 390px mobile hero were inspected visually. Mobile has no horizontal overflow, and both crew members remain visible in the photo.
- Only the two family-business photos animate on Home and Our Story. All ten other homepage photo frames have transform=none, clip=none and zero bleed, including the hero, services, project gallery and blog.
- Story travel drops from 72px to 18px in each direction on desktop and from 32px to 9px on mobile. Scrub smoothing increases from 0.45 to 1.2 seconds. Scale stays 1; no reveal mask is applied.
- At desktop scroll 2453, the story photos settle to y=-4.5489px and -6.7558px. At scroll 2774, they settle to y=4.4093px and 3.0792px. Both images cover their frames throughout, and copy/frame geometry stays fixed.
- Live reduced-motion emulation leaves every photo still and restores zero crop bleed. Clearing it restores the two story effects. At 390px, the two story transforms begin at -9px while all other photos remain still.
- With scripting disabled, photos remain still, mobile navigation stays visible, the original story remains present, and the down-link target exists. This checks static rendering and targets, rather than automated no-JavaScript activation. Scripting and motion emulation were restored afterward.
- Services and Portfolio load only app.js. Service photos are still and have no horizontal overflow at 390px. Commercial filtering still reports six projects, whose photos remain still.
- The accessibility page describes motion only in the family-business section. Email and quote delivery remain empty.

Screenshots in ignored artifacts/: crew-hero-desktop.png, crew-hero-mobile.png, gentle-story-entry.png and gentle-story-midpoint.png. The final browser preview is crew-hero-preview.png.

Final checks: all 27 HTML files pass the static validator; application JavaScript syntax checks pass; Design Taste scans 36 output/document files with zero hard violations and zero warnings. Git whitespace checks pass. Reverse scrolling retraces the story movement.
