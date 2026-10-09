# Montesinos Electric redesign

A portable, static website for Montesinos Electric, with a black-and-yellow design, the original logo, and photographs from the current Wix website. No framework or server dependency is needed to serve `dist/`.

## Preview

From this directory, run `python -m http.server 4173 --directory dist --bind 127.0.0.1`, then visit http://127.0.0.1:4173/.

## Content and pages

Edit `site-content.json` for the business story, contact information, service descriptions, project captions, and gallery images. `build_site.py` generates HTML pages. It uses Python and Pillow to prepare compressed images. The generated `dist/` is included and can be hosted directly. `page-inventory.json` lists the generated pages. `dist/styles.css` and `dist/app.js` contain the styling and interactions.

The site includes Home, Services, three service detail pages, Our Work, Our Story, Blog, three original project stories, Service Area, Contact / Free Quote, Website Privacy, Accessibility, and a 404 page. Old booking and service entry points route to the corresponding new pages. Gallery filters and keyboard-accessible photo dialogs work without a backend. Quote requests can be prepared and copied locally.

## Email and quotes

`business.email` and `business.quoteEndpoint` are deliberately empty, as requested. The website does not send, store, or pretend to submit contact requests. The form clearly prepares a local project summary and directs visitors to call (623) 202-2164. Connecting delivery requires a real server endpoint, validation, spam protection, and integration in `dist/app.js`; setting a field alone does not enable delivery.

The original site also lists (602) 516-4732; it is retained on the contact page. The primary number matches the supplied Google listing. Confirm the secondary number with the owner before launch.

## Publication

The Sites project ID and static directory live in `.openai/hosting.json`. This build is a private review site, with `noindex,nofollow` and a disallow-all robots.txt to avoid indexing duplicate content. The original Wix site and domain are unchanged. Before launching on the business domain, update `ORIGIN` in `build_site.py`, remove the preview indexing restrictions, regenerate the sitemap, connect quote delivery, and confirm service coverage and business details with the owner.

## Source and review

See `SOURCE-AUDIT.md` for the original page review and pending business details. See `SKILLS-RESEARCH.md` for the reusable skills researched and selected. Photos are optimized from originals with their subjects preserved; original files remain locally in ignored `source-assets/`. The wing-shaped logo is the original website mark, recolored black for the requested palette. Fonts are served locally.
