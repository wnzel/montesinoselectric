# Montesinos Electric design direction

Reading this as a local service-business website for Valley homeowners and businesses, using the Peraltas-inspired service-business-website template and Montesinos Electric's actual identity and work. Persuade mode for the public pages, Operate mode for quote preparation. DESIGN_VARIANCE 5, MOTION_INTENSITY 3, VISUAL_DENSITY 4: alternating large photographs, calm feedback and a clear path to contact.

This is a redesign with content preservation. The user's centered-text request takes precedence over the template's default left-aligned hero. Hero heading, description and actions share one center line. Section introductions, service copy, story copy, project captions, contact headings and the footer use consistent centered groups. Labels and input text stay left-aligned for readability; long legal prose keeps its readable measure.

The original wing-shaped logo, black/yellow branding, Source Sans 3 font, original job-site photos, family story, all three service meanings, twenty project captions, blog dates and both phone numbers remain. Business content lives in site-content.json. SOURCE-AUDIT.md records the original Wix and Google evidence. No reviews, ratings, social profiles, service cities, boundaries, credentials or promises were added. Existing URLs, redirects, metadata, JSON-LD, deployment settings and quote field contract remain.

Semantic tokens define accent, accent hover, page/secondary/form surfaces, text, muted text, borders, photo text and focus. The existing yellow is #FFE13B; text is #161616 and page surface #FEFEFD. Corners use 4px throughout, except the deliberately circular down control. The light theme supports reading service information and inspecting project photos in everyday daylight; the retained yellow bands and dark footer are existing brand treatments.

## Template composition

- Yellow utility banner and 80px sticky navigation: original mark left, Services overview plus separately operable dropdown, Gallery, About us, Blog, Contact us, quote and primary phone. Home navigation overlays the photo and turns white after 48px scroll. Below 1200px a hamburger panel replaces crowded desktop links; nested services, full-width quote and phone remain reachable.
- Full-screen crew-at-work photo with a Montesinos Electric label above the centered heading, sequenced text entrances, quote and Services actions, and the requested down shortcut. The photo remains still. It uses a bottom-aligned cover crop and a readable dark scrim.
- Three larger image-and-copy service rows, with right/left/right photo placement on desktop and image-before-copy stacking on phones. Their photos drift with the same gentle scroll motion as the About photos.
- Gallery introduction beside a manual native scroll-snap carousel: two projects wide, one on phones. Six real project photos, Next above Previous in a column to the right of the photos (as in the reference), screen-reader-only position feedback with no visible counter, and native swipe; no autoplay, duplicate loop copies or invented project stages. Existing photo dialog and dedicated gallery filters remain.
- Paired staggered About photos beside the original family story. These and the service photos drift slowly inside fixed frames, retaining 18px desktop/9px phone travel with 1.2-second scrub smoothing.
- A centered good-guy-price band uses only supported family ownership, license/insurance and experience claims. Valley map and original project stories remain useful additional sections. Project stories uses a warm tinted surface so it stays distinct from the grey map band above and the white quote section below.
- One shared quote component appears at the end of Home and on /contact/. Home quote links reach its heading; the dedicated contact route still works directly. Contact heading/details and all six form fields fit a first desktop screen. Phones stack heading, form, then contact information in both visual and DOM order. The Valley section follows normally on Contact.
- Larger centered footer logo, wrapped navigation, callable phone, privacy/accessibility links and copyright. No unsupported social destinations.

## Interaction and fallback

Services disclosure supports hover with a 150ms crossing grace, separate pointer/keyboard toggling, Escape, outside close and focus retention. The hamburger changes to a close mark, resets nested services on close and switches to an opaque header. CSS and JavaScript share the 1200px breakpoint.

One anchor coordinator handles pointer smooth scrolling and immediate keyboard/reduced-motion navigation. Real hrefs retain direct entry and modified-click behavior. Reduced motion stops text entrances, header transitions and story drift, including preference changes during a visit. Essential content remains visible without motion scripts. Without JavaScript, readable navigation, direct photo links and phone quote alternatives remain.

Prior user instructions limit photo animation to the family-business section. Template service parallax, hover zoom and detail media entrances are intentionally omitted. Reviews and timed multi-stage project slides are not applicable because no verified reviews or stage sets exist.

The form retains the existing local-summary workflow and unchanged requiredness, names, order, autocomplete and service values. Email and endpoint remain empty. It does not send a request; preparation and copy feedback say so clearly. No new CMS, backend, library or build dependency was introduced.
