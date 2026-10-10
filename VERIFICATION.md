# Verification, October 10, 2026 Vercel and photo hero

October 10 navbar and quote-page checks, locally and on Vercel:

- The local homepage navbar is transparent at the top, with white text and logo. At scrollY 216 it is white with dark text and remains at viewport top. Returning to the top restores the transparent state. The yellow banner remains above the photo.
- The hero ends at the viewport bottom and has no horizontal overflow. At 390 by 844, opening the menu switches its header and navigation to white with dark text; following Contact opens the quote page with a white header.
- The complete initial contact interface fits at 938 by 892, 1280 by 720, 1280 by 640 and 938 by 640. At 938 by 892, the form ends at 794px and the Valley section starts at 892px. At 938 by 640, contact details end at 609px, the form ends at 601px and the Valley section starts at 640px.
- All six quote fields remain. Mobile has one column and no horizontal overflow. Submitting an empty form focuses the required name field and keeps the summary hidden. A synthetic valid request produces the correct local summary and focuses its heading. No request is sent.
- Reduced motion disables header transitions and leaves photos still. With JavaScript disabled, the header remains white with dark text and the hero image loads. Development emulation is restored afterward. No browser application errors were observed.

The Vercel production deployment of 7f00af1 passes the same live navbar and contact checks. At the review viewport, the form ends at 794px and the Valley section starts at 892px. Ordinary scrolling moves the Valley section into view, with the white header staying at the top. An additional polish pass enables header fades only after the initial transparent state has painted, preventing a gray strip on page load. Screenshots in ignored artifacts/: blended-navbar-live.png, white-navbar-on-scroll-live.png and quote-first-screen-live.png.

The public deployment at https://montesinoselectric.vercel.app/ is working. Before the fix, its root returned Vercel's NOT_FOUND 404 while /dist/ returned the website HTML. Commit 7fc7506 adds the static output configuration and full-width crew-photo hero. Vercel's GitHub status reports a successful production deployment for that commit.

- Vercel now publishes only dist at the site root, with no install or build step. Generated canonical URLs, social metadata, structured data and the sitemap use the verified Vercel review domain.
- All 27 HTML files pass the static validator. Local HTTP checks serve 64 page and asset files. Live HTTP checks pass for 73 page, asset and directory URLs, including services, project stories and the original booking entry point. An unknown live route returns the branded 404 page with HTTP 404.
- Visual checks on the live site pass at 1280 by 900, 1280 by 640, 390 by 844 and 320 by 760. The landscape crew photo fills the hero width, stays still, and crops from the bottom to retain the workers. Text and contact actions remain visible, with no horizontal overflow. The source photo is unchanged.
- The mobile menu opens and closes with Escape. Keyboard activation of the circular down link reaches Electrical Services, places its top below the sticky header, and focuses the target. Service images remain still.
- Only the two family-business photos receive transforms. Live reduced-motion emulation restores still photos and zero bleed. With JavaScript disabled, the hero image loads, the down-link target remains valid, and desktop content has no horizontal overflow. Emulation was restored after the checks.
- Gallery navigation opens the correct page. Commercial filtering shows six projects; the photo dialog opens, advances to the second photo, closes with Escape, and restores focus to the triggering link.
- The Google map automatically loads Valley map tiles on the live site. No application console errors were observed. An earlier Vercel login page logged a Google sign-in network error before the public domain was opened; it is unrelated to the application.
- Application JavaScript syntax and Git whitespace checks pass. Design Taste scans 34 output and design-document files with zero hard violations and warnings. Email and quote delivery remain unconfigured as requested.

Screenshots are in ignored artifacts/: full-photo-hero-desktop.png, full-photo-hero-mobile.png and full-photo-hero-preview.png. Viewport, reduced-motion and scripting overrides were reset. The live homepage is left open for review; localhost serves the same committed dist files at http://127.0.0.1:4173/.

## Earlier verification, October 9, 2026 crew-photo refinement

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
