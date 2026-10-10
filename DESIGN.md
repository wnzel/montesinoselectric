# Montesinos Electric design direction

A practical Valley contractor website with readable typography and the company's actual work supplying its character. This is a refinement of the existing redesign, using static HTML, CSS and locally served GSAP. Design variance 4, motion intensity 2, visual density 4.

Use the original wing-shaped mark and existing photos. The company's “The good guy price” tagline remains on the story page and in the footer. The homepage names the service and location directly. Keep pages, navigation labels, contact fields and URL structure.

Use Source Sans 3 throughout: headings 650, body 400, navigation/buttons 600. The font is self-hosted as a variable WOFF2 file. Palette: yellow #FFE13B, near-black #161616, paper #FEFEFD, light neutral #F3F4F0, muted copy #555750, divider #D9DCD4. Use 2px corners. Light content areas serve reading and inspecting daylight photographs; the black footer and yellow contact band continue the requested brand palette.

Remove floating badges, decorative icons and arrows on routine links. Add captions only when they identify the actual work. Services form a short list with photos; the gallery groups project photos; the blog gives one collection more space beside two smaller stories. Layouts stack on mobile.

Write plainly about the work. Remove em dashes and generic slogans from new copy. Preserve the original family-business story. Do not add unsupported ratings, testimonials, response times, warranties, prices, founding dates, exact service boundaries or license numbers.

Quote delivery stays unconfigured per the user. Visitors can prepare and copy project details, then call the verified number. Email remains empty in site-content.json. See DESIGN-REVIEW.md for the visual review and RECENT-DESIGN-SKILLS.md for dated skill sources.

The homepage opens with “Your Valley electricians.” over a landscape job-site photo of the actual crew installing ceiling lights. The photo covers the full hero width and fills the first screen below the header, matching the background-photo structure of the user's Peraltas Roofing site. A dark overlay keeps the left-aligned copy readable; quote and phone actions sit beneath it. The hero stays still. CSS uses a bottom-aligned cover crop to retain the workers, including on mobile, without altering the source photo. The circular down link reaches a labelled Electrical Services section. The previously removed opening photo and caption remain absent from this hero. Utility text, service area, contact copy, metadata and structured data describe the Valley (Greater Phoenix area); the business location remains Phoenix. The regional map loads automatically, without adding a business coverage polygon or a new city list.

Cinematic Scroll's editorial recipe informs one gentle moment: the two photos in the family-owned business section drift from -18px to +18px, with 1.2-second scrub smoothing. Mobile uses 9px travel. No photo zoom or reveal mask is applied. Hero, service, gallery and blog photos remain still. GSAP 3.15.0 and ScrollTrigger are loaded only on Home and Our Story, where the shared family-business section appears. Each story image owns its transform; surrounding copy and frame geometry stay fixed. Reverse scrolling retraces the movement, and reduced motion reverts it. Script failure and no-JavaScript mode leave full still photos and useful actions.
