# Montesinos Electric design direction

A practical Valley contractor website with readable typography and the company's actual work supplying its character. This is a refinement of the existing redesign, using static HTML, CSS and locally served GSAP. Design variance 4, motion intensity 5, visual density 4.

Use the original wing-shaped mark and existing photos. The company's “The good guy price” tagline remains on the story page and in the footer. The homepage names the service and location directly. Keep pages, navigation labels, contact fields and URL structure.

Use Source Sans 3 throughout: headings 650, body 400, navigation/buttons 600. The font is self-hosted as a variable WOFF2 file. Palette: yellow #FFE13B, near-black #161616, paper #FEFEFD, light neutral #F3F4F0, muted copy #555750, divider #D9DCD4. Use 2px corners. Light content areas serve reading and inspecting daylight photographs; the black footer and yellow contact band continue the requested brand palette.

Remove floating badges, decorative icons and arrows on routine links. Add captions only when they identify the actual work. Services form a short list with photos; the gallery groups project photos; the blog gives one collection more space beside two smaller stories. Layouts stack on mobile.

Write plainly about the work. Remove em dashes and generic slogans from new copy. Preserve the original family-business story. Do not add unsupported ratings, testimonials, response times, warranties, prices, founding dates, exact service boundaries or license numbers.

Quote delivery stays unconfigured per the user. Visitors can prepare and copy project details, then call the verified number. Email remains empty in site-content.json. See DESIGN-REVIEW.md for the visual review and RECENT-DESIGN-SKILLS.md for dated skill sources.

The homepage opens with “Your Valley electricians.” in a split hero that fills the desktop viewport. Copy and quote actions sit on the left; an original lighting and ceiling fan project photo fills the right. The circular down link reaches a labelled Electrical Services section. Mobile uses natural stacked flow. The previously removed opening photo and caption remain absent from this hero. Utility text, service area, contact copy, metadata and structured data describe the Valley (Greater Phoenix area); the business location remains Phoenix. The regional map loads automatically, without adding a business coverage polygon or a new city list.

Cinematic Scroll's editorial recipe informs the photo movement, and the official GSAP ScrollTrigger skill informs its implementation. GSAP 3.15.0 supplies the scroll clock; each image owns its transform and each frame owns its reveal. Photos enter enlarged with 18% of the lower edge clipped, open to their full frame, and move from -72px to +72px while zooming from 1.12 to 1. Their position holds after the short scrub smoothing settles. Reverse scrolling retraces the movement. The hero starts fully revealed; other initially visible photos render at their correct scroll progress. Mobile uses 32px travel. All photo effects revert when reduced motion is enabled. Missing scripts and no-JavaScript mode show complete still photos with the useful copy and contact actions. There are no pinned scenes or page-wide scroll overrides.
