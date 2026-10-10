# Montesinos Electric redesign

A portable, static website for Montesinos Electric, serving the Valley, with a black-and-yellow design, the original logo, and photographs from the current Wix website. No framework or server dependency is needed to serve `dist/`.

## Preview

From this directory, run `python preview_server.py`, then visit [localhost](http://127.0.0.1:4173/). The preview server serves the latest files without caching them.

## Content and pages

Edit `site-content.json` for the business story, contact information, service descriptions, project captions, and gallery images. `build_site.py` generates HTML pages. It uses Python and Pillow to prepare compressed images. The generated `dist/` is included and can be hosted directly. `page-inventory.json` lists the generated pages. `dist/styles.css` and `dist/app.js` contain the styling and interactions.

The site includes Home, Services, three service detail pages, Our Work, Our Story, Blog, three original project stories, Service Area, Contact / Free Quote, Website Privacy, Accessibility, and a 404 page. Old booking and service entry points route to the corresponding new pages. Gallery filters and keyboard-accessible photo dialogs work without a backend. Quote requests can be prepared and copied locally.

## Email and quotes

`business.email` and `business.quoteEndpoint` are deliberately empty, as requested. The website does not send, store, or pretend to submit contact requests. The form clearly prepares a local project summary and directs visitors to call (623) 202-2164. Connecting delivery requires a real server endpoint, validation, spam protection, and integration in `dist/app.js`; setting a field alone does not enable delivery.

The original site also lists (602) 516-4732; it is retained on the contact page. The primary number matches the supplied Google listing. Confirm the secondary number with the owner before launch.

## Publication

The Sites project ID and static directory live in `.openai/hosting.json`. This build is a private review site, with `noindex,nofollow` and a disallow-all robots.txt to avoid indexing duplicate content. The original Wix site and domain are unchanged. Before launching on the business domain, update `ORIGIN` in `build_site.py`, remove the preview indexing restrictions, regenerate the sitemap, connect quote delivery, and confirm service coverage and business details with the owner.

## Source and review

See `SOURCE-AUDIT.md` for the original page review and pending business details, `RECENT-DESIGN-SKILLS.md` for the October 9 skills search, and `DESIGN-REVIEW.md` for the visual review. Photos are optimized from originals with their subjects preserved; originals remain locally in ignored `source-assets/`. The original wing-shaped mark is recolored black for the requested palette. Source Sans 3 is served locally as a 29 KB variable WOFF2 font; its license is included with the asset.

## Photo motion

Project, service and team photographs drift gently inside cropped frames as visitors scroll. Native CSS view timelines are a progressive enhancement; text and layout stay fixed. Phone layouts use less travel. Reduced-motion settings and browsers without scroll-timeline support show still photographs. No animation library or build-time JavaScript dependency is required. With JavaScript disabled, navigation and direct photo links remain available; quote requests are directed to the phone number.

## GitHub

Source and generated output are maintained on `main` at [wnzel/montesinoselectric](https://github.com/wnzel/montesinoselectric). Pushing this repository does not deploy the business domain.
