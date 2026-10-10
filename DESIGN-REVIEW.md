# Design review, October 9, 2026

Read this as a local contractor website for Valley homeowners and businesses, with practical typography and the company's own photographs. Persuade mode; static site with locally served GSAP photo effects. Design variance 4, motion intensity 2, density 4: structured layouts, photo motion tied to scrolling, easy access to services and contact details. Humanizer and Design Taste informed the refinement.

| Before | After | Why |
| --- | --- | --- |
| Condensed display headings and a separate body font | One self-hosted Source Sans 3 family | Clearer letterforms and consistent reading. |
| “From the first wire to the final fixture” | “Electrical services” with specific descriptions | Visitors immediately understand the content. |
| Floating photo badges and decorative icons | Unobstructed project photos and useful captions | Actual work supplies the character. |
| Arrows on routine links and buttons | Descriptive labels and underlined text links | Familiar cues with less visual noise. |
| Repeating service and blog cards | Service rows, project photos and a varied blog layout | Each section fits its content. |
| Em dash in the quote summary and title | Colon | Matches the requested punctuation preference. |
| Fake streets before the map loads | Plain map loading control | Does not present decoration as geography. |
| Blog description initially placed in the image column | Only the image link spans grid rows | Corrected during desktop visual review. |

Original business story, photos, logo mark, navigation labels, routes, contact fields and order, phone numbers and legal page body copy are preserved. The user authorized typography, wording and icon changes and requested the original black/yellow identity and photographs. Light content areas serve reading and inspecting daylight photos; the black footer and yellow contact band continue the requested palette.

Universal Core checklist results:

| Check | Result |
| --- | --- |
| Mode, brief and dials | Declared above; one native CSS system. |
| Redesign audit | Reviewed brand tokens, content, routes, conversion paths and existing accessibility behavior. |
| Zero em dashes | None in rendered copy or prepared quote summary. |
| Theme, accent and shape locks | Light content theme, brand yellow and 2px corners; footer/contact band use requested brand colors. |
| Contrast | Normal text, button text, muted copy, labels, placeholders and focus colors checked. |
| Type discipline | Desktop CTA labels stay on one line; no italic display type or serif pairing. |
| Copy self-audit | New copy checked against original business information; original story retained by request. |
| Motion | Cropped photo parallax, fixed copy, smaller mobile travel; live reduced-motion and static fallbacks. |
| Dark mode | Locked light theme for service reading and inspecting daylight photographs. |
| Responsive | Desktop and mobile reviewed, including 320px; layouts stack below 768px. |
| Interaction states | Native form validation, local summary, clipboard fallback, selected filters, menu states and native photo dialog retained. The map connects to Google automatically, as described on the privacy page. |
| Layout restraint | No decorative status dots or service boxes; separators organize the short service list. |
| No fake visuals | Original photos/logo only; decorative icons and false street illustration removed. |
| Fake-precise numbers | None added; original experience claim and photo captions preserved. |
| No generic design tells | Plain headings, one purposeful font family, specific services and actual business assets. |
| Core Web Vitals | No formal benchmark. Explicit image dimensions, eager hero photo, lazy supporting images and 29 KB local WOFF2 font reduce loading work and layout shifts. |

Persuade checklist results:

| Check | Result |
| --- | --- |
| Navigation | One line at desktop, 80px tall; collapses at narrower widths. |
| Persuade-specific patterns | Service rows instead of equal feature cards; actual project photos. |
| Premium-consumer palette | N/A: contractor site. |
| Content density | Short introductions; full project collections have their own pages; original story retained by request. |
| Real images | Existing company photos required by user; no generated assets. |
| Hero fits viewport | Full viewport on desktop, with right-side photo and left-side heading, description and actions. Mobile stacks naturally. |
| Hero top padding | 40px desktop, 28px on shorter desktop viewports, 36px mobile. |
| Hero stack | License label, headline, description and actions. |
| Eyebrow count | No repeated uppercase section labels. |
| Split-header ban | Descriptions below headings; section navigation links beside them. |
| Zigzag cap | Two consecutive split layouts: story and service area. |
| Duplicate CTA intent | Quote actions repeat in navigation, relevant content and footer for access; no differently worded competing contact actions. |
| Logo wall labels | N/A: no logo wall. |
| Bento background diversity | N/A: no bento. |
| Trust logo wall | N/A: no trust logos. |
| Marquee count | N/A: no marquee. |
| Section-layout repetition | Full-height split hero, larger service photos in rows, project photos, paired team photos and varied journal layout. |
| Bento cell rhythm | N/A: no bento. |
| Photo overlays | Removed. |
| Decorative photo credits | None; the new hero uses an original project photo without a decorative caption. |
| Version footers | None. |
| Micro-meta sentences | None. |
| Hero decoration strip | Removed. |
| Floating corner description | None. |
| Scoring/progress bars | N/A: no scoring. |
| Locale strips | The Valley identifies service coverage for the local-business brief; no clocks or weather decoration. |
| Scroll cues | The circular down link is explicitly requested by the user and reaches Electrical Services. |
| Hero version labels | None. |
| Numbered section labels | None. |
| Quote length | N/A: no testimonials. |

Mechanical preflight and project validator pass. Browser review covers desktop, mobile navigation, narrow page layouts, gallery filtering, photo advancement, Escape/focus restoration, and the local quote summary. Screenshots are under ignored `artifacts/`. The server remains running for the user's requested localhost review.

## Earlier Valley and motion refinement (superseded by the fullscreen follow-up)

| Before | After | Why |
| --- | --- | --- |
| Homepage identifies Phoenix only | “Your Valley electricians.” with regional copy and schema | Reflect the user-confirmed coverage across the Valley. |
| Opening new-home photo | Text-led opening with the quote and phone beside the heading | Remove the specific photo the user requested. |
| Still photo crops | Photos drift within fixed frames while reading copy stays steady | Match the Peralta's cropped parallax reference without changing page flow. |
| Viewer triggers require JavaScript | Photo links target their original full-size image and enhance into dialogs | Keep project imagery available in the static fallback. |

## Earlier fullscreen hero and stronger motion follow-up

The hero now fills the desktop viewport with an original lighting project photo on the right, and the quote/phone actions under the introduction on the left. The down-circle is a native anchor with a meaningful target and visible keyboard focus. Service photos grow from 170 × 132px to 300 × 220px on desktop and fill the row width on phones. “The good guy price” remains in the story and footer.

The browser-dependent native timeline is replaced by GSAP ScrollTrigger. Photos reveal, zoom out and drift with scroll; reverse scrolling retraces the effect. Copy stays still. Live media changes clean up all owned styles/triggers. Initially visible photos now reveal fully, correcting an edge case found during testing. Maps render automatically, with redundant listing buttons removed.

See VERIFICATION.md for the current browser evidence and fallback checks.

## Current crew photo and calmer story motion

The hero uses the original utility-piping crew photo with its crop centered on the people. The two family-business photos are the only images with scroll motion, on Home and Our Story. Their travel drops 75% to 18px on desktop and 9px on phones; smoothing increases to 1.2 seconds. Zoom and reveal clipping are removed. Other photos remain still, and pages without that section no longer load animation scripts. The accessibility copy now describes this scope.
