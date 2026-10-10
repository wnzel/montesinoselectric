"""Generate portable static pages from the editable business content."""
import json,html,re,shutil
from pathlib import Path
from PIL import Image,ImageOps

ROOT=Path(__file__).parent
DIST=ROOT/'dist'
DATA=json.loads((ROOT/'site-content.json').read_text(encoding='utf-8'))
B=DATA['business'];SERVICES=DATA['services'];PROJECTS=DATA['projects']
ORIGIN='https://montesinoselectric.vercel.app'
e=lambda s:html.escape(str(s),quote=True)

def button(label,href,style=''):return f'<a class="button {style}" href="{e(href)}">{label}</a>'
def textlink(label,href):return f'<a class="text-link" href="{e(href)}">{label}</a>'

def image(file,alt,cls='',eager=False):
    source=DIST/'assets'/file
    webp=source.with_suffix('.webp')
    with Image.open(webp) as photo:
        width,height=photo.size
    return f'<img src="/assets/{e(webp.name)}" alt="{e(alt)}" width="{width}" height="{height}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'

def photo(file,alt,cls='',eager=False):
    return f'<div class="photo-frame {cls}">{image(file,alt,eager=eager)}</div>'

# Preserve originals outside the deployment and serve compressed copies.
originals=ROOT/'source-assets';originals.mkdir(exist_ok=True)
for source in list((DIST/'assets').glob('b491a5*')):
    if source.suffix=='.webp':continue
    shutil.copy2(source,originals/source.name)
    with Image.open(source) as photo:
        photo=ImageOps.exif_transpose(photo).convert('RGB');photo.thumbnail((1800,1800))
        photo.save(source.with_suffix('.webp'),'WEBP',quality=84,method=6)
    source.unlink()
for source in originals.glob('b491a5*'):
    dest=DIST/'assets'/source.with_suffix('.webp').name
    if dest.exists():continue
    with Image.open(source) as photo:
        photo=ImageOps.exif_transpose(photo).convert('RGB');photo.thumbnail((1800,1800));photo.save(dest,'WEBP',quality=84,method=6)
logo=(ROOT/'logo-source.svg').read_text(encoding='utf-8')
logo=re.sub(r'<defs>.*?</defs>','',logo,flags=re.S).replace('viewbox=','viewBox=').replace('preserveaspectratio="none"','preserveAspectRatio="xMidYMid meet"').replace('fill="#FFB39E"','fill="#000000"')
(DIST/'assets'/'logo.svg').write_text(logo,encoding='utf-8')

def brand():return '<a class="brand" href="/" aria-label="Montesinos Electric home"><img src="/assets/logo.svg" alt="" width="35" height="40"><strong>MONTESINOS<span>ELECTRIC</span></strong></a>'
NAV=[('Gallery','/portfolio/'),('About us','/about/'),('Blog','/blog/')]
def header(active,home=False):
    links=''.join(f'<a href="{path}"'+(' aria-current="page"' if path==active else '')+f'>{label}</a>' for label,path in NAV)
    service_links=''.join(f'<a href="/services/{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    services=f'<div class="services-nav"><div class="services-trigger"><a href="/services/"'+(' aria-current="page"' if active=='/services/' else '')+f'>Services</a><button class="services-toggle" type="button" aria-label="Show electrical services" aria-expanded="false" aria-controls="service-navigation"><span class="chevron" aria-hidden="true"></span></button></div><div class="services-panel" id="service-navigation" hidden>{service_links}<a href="/service-area/">Valley service area</a></div></div>'
    sentinel='<span class="header-sentinel" aria-hidden="true"></span>' if home else ''
    quote='#request-quote' if home else '/contact/'
    return f'''<a class="skip" href="#main">Skip to content</a><div class="utility"><div class="wrap"><span class="local-line">Family-owned electrical service across the Valley</span><a href="tel:{B['phoneLink']}">Hablamos español &nbsp; {B['phone']}</a></div>{sentinel}</div><header class="header"><nav class="nav wrap" aria-label="Main navigation">{brand()}<button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="navigation"><span class="menu-lines" aria-hidden="true"></span><span class="menu-label">Menu</span></button><div class="navlinks" id="navigation">{services}{links}<a href="/contact/">Contact us</a>{button('Free quote',quote)}<a class="nav-phone" href="tel:{B['phoneLink']}">{B['phone']}</a></div></nav></header>'''
def footer():
    return f'''<footer class="footer"><div class="wrap">{brand()}<p>Family-owned electrical services. The good guy price.</p><nav class="footer-nav" aria-label="Footer navigation"><a href="/about/">About us</a><a href="/portfolio/">Gallery</a><a href="/services/">Services</a><a href="/blog/">Blog</a><a href="/contact/">Contact us</a><a href="/service-area/">Service area</a></nav><a class="phone" href="tel:{B['phoneLink']}">{B['phone']}</a><p>Hablamos español. Serving the Valley.</p><div class="footer-bottom"><div><a href="/privacy/">Website privacy</a><a href="/accessibility/">Accessibility</a></div><span>© 2026 Montesinos Electric. All rights reserved.</span></div></div></footer><div class="mobile-contact"><a href="tel:{B['phoneLink']}">Call Montesinos</a><a href="/contact/">Free quote</a></div>'''
def cta():return f'<section class="cta"><div class="wrap"><div><h2>Have an electrical project?</h2><p>Call Montesinos Electric to discuss the work and get a free quote.</p></div><div class="cta-actions">{button("Get a free quote","/contact/")}{button(B["phone"],"tel:"+B["phoneLink"],"outline")}</div></div></section>'
def lightbox():return '<dialog class="lightbox" aria-labelledby="photo-title"><div class="lightbox-header"><h2 id="photo-title"></h2><button class="lightbox-close" aria-label="Close photo">✕</button></div><img class="lightbox-image" alt=""><div class="lightbox-controls"><button class="lightbox-prev" aria-label="Previous photo">‹</button><span class="lightbox-count" aria-live="polite"></span><button class="lightbox-next" aria-label="Next photo">›</button></div></dialog>'
def project(p):
    src='/assets/'+Path(p['image']).with_suffix('.webp').name
    return f'''<article class="project-card" data-category="{p['category']}"><a class="project-open" href="{src}" data-image="{src}" data-title="{e(p['title'])}" data-category="{p['category']}" aria-label="View photo: {e(p['title'])}"><div class="project-image photo-frame">{image(p['image'],p['title'])}</div><div class="project-meta"><span>{p['category']}</span><h3>{e(p['title'])}</h3></div></a></article>'''
def service(s):return f'<article class="service-row"><a class="service-thumb" href="/services/{s["slug"]}/" aria-label="Learn about {s["name"]}">{photo(s["image"],s["name"]+" by Montesinos Electric")}</a><div class="service-body"><h3><a href="/services/{s["slug"]}/">{s["name"]}</a></h3><p>{s["short"]}</p>{button("Explore this service","/services/"+s["slug"]+"/","outline")}</div></article>'
POSTS=[('residential','Residential','Panels and lighting for homes','Panels, utility connections, lighting, fans, and outlet wiring for homes.'),('commercial','Commercial','Commercial installations','Lighting, car wash equipment, panels, and conduit for commercial spaces.'),('industrial','Industrial','Motors and industrial equipment','Three-phase motors, compressors, switches, and conduit installations.')]
def blogcard(post):
    slug,category,title,desc=post
    representative={'Residential':PROJECTS[0],'Commercial':PROJECTS[7],'Industrial':PROJECTS[13]}[category]
    return f'''<article class="blog-card"><a href="/post/{slug}/" aria-label="Read {category} project story">{photo(representative['image'],representative['title'])}</a><div class="post-meta"><span>{category}</span><time datetime="2025-10-29">Oct 29, 2025</time></div><h3><a href="/post/{slug}/">{title}</a></h3><p>{desc}</p>{textlink('Read project story','/post/'+slug+'/')}</article>'''
def mapblock():return '<div class="map-panel"><iframe title="Greater Phoenix area (the Valley) map" src="https://www.google.com/maps?q=Phoenix%2C%20Arizona&amp;z=9&amp;output=embed" width="640" height="360" loading="eager" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'
def area():return f'<section class="section area"><div class="wrap area-grid"><div class="area-copy"><h2>Serving the<br>Valley</h2><p>Tell us where your project is located. We’ll confirm availability for your address and discuss the electrical work you need.</p></div>{mapblock()}</div></section>'
def story():return f'<section class="section"><div class="wrap story-grid"><div class="story-photos">{photo("b491a5_c102ea168a4c4b76956029cafde38851~mv2.jpg","Montesinos Electric team installing lighting","large")}{photo("b491a5_34c9b999e8984462b71b9c1979b3d321~mv2.jpeg","Montesinos Electric crew working on utility piping","small")}</div><div class="story-copy"><h2>A family-owned electrical business</h2><p>{B["story"]}</p>{textlink("Meet Montesinos Electric","/about/")}</div></div></section>'
def intro(title,copy,crumb=''):
    return f'<section class="page-intro"><div class="wrap"><div class="breadcrumb"><a href="/">Home</a><span>/</span>{crumb or e(title)}</div><h1>{title}</h1><p>{copy}</p></div></section>'
def quote_section(home=False):
    heading = '<h2 id="quote-title">Request a free quote</h2>' if home else '<h1 id="quote-title">Request a free quote</h1>'
    return f'''<section class="{"section " if home else ""}contact-screen quote-section" id="request-quote" tabindex="-1" aria-labelledby="quote-title"><div class="wrap contact-layout">
  <div class="contact-heading">
    <div class="breadcrumb"><a href="/">Home</a><span>/</span>Contact &amp; free quote</div>
    {heading}
    <p>Call our team or prepare your project details below.</p>
  </div>
  <div class="contact-form-panel"><form class="quote-form" id="quote-form">
    <h2>Your project details</h2>
    <p class="form-intro">Prepare a summary to copy and share. It does not send your request.</p>
    <div class="form-grid">
      <div class="field"><label for="name">Your name *</label><input id="name" name="name" autocomplete="name" required maxlength="120" placeholder="First and last name"></div>
      <div class="field"><label for="phone">Phone number *</label><input id="phone" name="phone" type="tel" autocomplete="tel" required maxlength="30" placeholder="(602) 555-0123"></div>
      <div class="field"><label for="email">Email <small>(optional)</small></label><input id="email" name="email" type="email" autocomplete="email" maxlength="200" placeholder="you@example.com"></div>
      <div class="field location-field"><label for="location">Project city or ZIP code *</label><input id="location" name="location" autocomplete="address-level2" required maxlength="120" placeholder="Phoenix, AZ"></div>
      <div class="field service-field"><label for="service">What can we help with? *</label><select id="service" name="service" required><option value="">Select a service</option>{''.join(f'<option value="{s["slug"]}">{s["name"]}</option>' for s in SERVICES)}<option value="other">Other electrical project</option></select></div>
      <div class="field wide"><label for="details">Tell us about your project *</label><textarea id="details" name="details" required maxlength="5000" placeholder="What needs to be installed, built, or fixed?"></textarea></div>
    </div>
    <button class="button" type="submit">Prepare my quote request</button>
    <p class="form-note">Details stay in your browser. <a href="/privacy/">Website privacy</a></p>
    <section class="quote-result" id="quote-result" hidden aria-labelledby="result-title"><h3 id="result-title" tabindex="-1">Your project details are ready.</h3><p>These details have not been sent. Call {B['phone']} to arrange your free quote, or copy your request to share with the team.</p><label class="sr-only" for="request-summary">Your prepared quote request</label><textarea id="request-summary" readonly></textarea><div class="result-actions">{button('Call Montesinos Electric','tel:'+B['phoneLink'])}<button type="button" class="button outline" id="copy-request">Copy request details</button></div><p id="copy-status" role="status" style="margin-top:12px"></p></section>
  </form><noscript><p>Call <a class="text-link" href="tel:{B["phoneLink"]}">{B["phone"]}</a> to discuss your project and request a free quote.</p></noscript></div>
  <aside class="contact-details" aria-label="Contact information">
    <div class="contact-item"><span>Call Montesinos Electric</span><a href="tel:{B['phoneLink']}">{B['phone']}</a><p>Hablamos español.</p></div>
    <div class="contact-item"><span>Additional phone</span><a href="tel:+16025164732">{B['additionalPhone']}</a></div>
    <div class="contact-item"><span>Service area</span><strong>The Valley, Arizona</strong><p>Call to confirm availability for your project location.</p></div>
  </aside>
</div></section>'''

PAGES={}
def save(path,title,description,content,active='',schema=None):
    url=ORIGIN+path
    business={'@context':'https://schema.org','@type':'Electrician','@id':ORIGIN+'/#business','name':B['name'],'url':ORIGIN+'/', 'telephone':B['phoneLink'],'logo':ORIGIN+'/assets/logo.svg','image':ORIGIN+'/assets/b491a5_c102ea168a4c4b76956029cafde38851~mv2.webp','description':'Family-owned electrical installation, troubleshooting, and maintenance across the Valley.','areaServed':{'@type':'Place','name':B['serviceArea']},'sameAs':[B['mapsUrl']]}
    ld=[business]+([schema] if schema else [])
    motion_scripts='<script defer src="/vendor/gsap.min.js"></script><script defer src="/vendor/ScrollTrigger.min.js"></script><script defer src="/motion.js"></script>' if 'story-photos' in content or 'service-row' in content else ''
    doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Montesinos Electric</title><meta name="description" content="{e(description)}"><meta name="robots" content="noindex,nofollow"><link rel="canonical" href="{url}"><meta property="og:type" content="website"><meta property="og:title" content="{e(title)} | Montesinos Electric"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN}/assets/b491a5_c102ea168a4c4b76956029cafde38851~mv2.webp"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#ffe13b"><link rel="icon" href="/assets/logo.svg" type="image/svg+xml"><link rel="preload" href="/assets/source-sans-3.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/styles.css"><script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>{motion_scripts}<script defer src="/app.js"></script><noscript><link rel="stylesheet" href="/no-script.css"></noscript></head><body class="{"home-page" if path=="/" else "contact-page" if path=="/contact/" else ""}">{header(active,home=path=="/")}<main id="main">{content}</main>{footer()}{lightbox()}</body></html>'''
    destination=DIST/path.strip('/')/'index.html' if path!='/' else DIST/'index.html'
    destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text(doc,encoding='utf-8');PAGES[path]=title

home=f'''<section class="hero" aria-labelledby="hero-title">
  <div class="hero-photo">{image("b491a5_c102ea168a4c4b76956029cafde38851~mv2.jpg","Montesinos Electric crew installing ceiling lights at a job site",eager=True)}</div>
  <div class="wrap hero-content"><div class="hero-copy">
    <p class="location">Montesinos Electric</p>
    <h1 id="hero-title">Your Valley<br>electricians.</h1>
    <p class="intro">Installation, troubleshooting and maintenance for homes, businesses and industrial spaces.</p>
    <div class="hero-actions">{button('Get a free quote <span class="button-arrow" aria-hidden="true">→</span>','#request-quote')}<a class="button on-photo" href="/services/">Explore services</a></div>
  </div></div>
  <a class="hero-down" href="#electrical-services" aria-label="Explore electrical services"><span aria-hidden="true">↓</span></a>
</section>
<section class="section wrap" id="electrical-services" tabindex="-1" aria-labelledby="services-title"><div class="section-head"><div><h2 id="services-title">Electrical services</h2><p>Start with a free quote for new construction, fixture installation or an electrical problem.</p></div>{textlink('Explore all services','/services/')}</div><div class="service-list">{''.join(service(s) for s in SERVICES)}</div></section>
<section class="section work-section"><div class="wrap gallery-preview"><div class="gallery-intro"><h2>Our electrical work</h2><p>Residential, commercial and industrial projects from our team.</p>{textlink('Explore the gallery','/portfolio/')}</div><div class="project-slider" role="region" aria-roledescription="carousel" aria-label="Featured electrical projects"><div class="gallery-track" id="featured-projects">{''.join(project(PROJECTS[i]) for i in [0,7,13,2,8,14])}</div><div class="carousel-controls" hidden><button type="button" class="carousel-next" aria-label="Next projects" aria-controls="featured-projects"><span aria-hidden="true">→</span></button><button type="button" class="carousel-prev" aria-label="Previous projects" aria-controls="featured-projects"><span aria-hidden="true">←</span></button><span class="carousel-status sr-only" role="status" aria-live="polite"></span></div></div></div></section>
{story()}<section class="value-band"><div class="wrap"><h2>The good guy price.</h2><p>Competitive pricing and clear communication about your electrical work.</p><ul><li>Family-owned</li><li>Licensed &amp; insured</li><li>Nearly 20 years of electrical experience</li></ul></div></section>{area()}

<section class="section stories-section"><div class="wrap"><div class="section-head"><div><h2>Project stories</h2><p>Browse our residential, commercial and industrial project collections.</p></div>{textlink('Visit the blog','/blog/')}</div><div class="journal-grid">{''.join(blogcard(p) for p in POSTS)}</div></div></section>{quote_section(home=True)}'''
save('/','Valley Electricians: The Good Guy Price','Family-owned electrical services across the Valley. Explore real residential, commercial and industrial work. Call (623) 202-2164 for a free quote.',home)

faq='<section class="section area"><div class="wrap faq"><h2>Common questions</h2><details><summary>Do you offer free quotes?</summary><p>Yes. Ground-up service, fixture installation, and troubleshooting are all available with a free quote. Call us to discuss the scope of your project.</p></details><details><summary>Do you work on homes and businesses?</summary><p>Our existing projects include residential, commercial, and industrial electrical work. Explore the gallery to see examples.</p></details><details><summary>Can I speak with someone in Spanish?</summary><p>Sí. Llame al (623) 202-2164 para hablar sobre su proyecto.</p></details><details><summary>How do I get started?</summary><p>Call (623) 202-2164 or prepare your project details on our free quote page. Have your location and a short description of the work ready.</p></details></div></section>'
save('/services/','Electrical Services Across the Valley','Ground-up electrical service, fixture installation and troubleshooting from Montesinos Electric. Free project quotes across the Valley.',intro('Electrical services','New construction, fixture installation and troubleshooting. Call to discuss your project and request a free quote.','Services')+f'<section class="page-content wrap"><div class="service-list">{"".join(service(s) for s in SERVICES)}</div></section>'+faq+cta(),'/services/')
for s in SERVICES:
    content=intro(s['name'],s['short'],f'<a href="/services/">Services</a><span>/</span>{s["name"]}')+f'''<section class="page-content wrap detail-grid">{photo(s['image'],s['name'],'detail-image',eager=True)}<div class="detail-copy"><span class="quote-tag">Free quote</span><h2>What this service covers</h2><p>{s['description']}</p><p>Examples of our work:</p><ul>{''.join('<li>'+e(t)+'</li>' for t in s['examples'])}</ul>{button('Get a free quote','/contact/?service='+s['slug'])}<p style="margin-top:20px;font-size:12px">Prefer to talk? <a href="tel:{B['phoneLink']}">{B['phone']}</a></p></div></section>'''+cta()
    schema={'@context':'https://schema.org','@type':'Service','name':s['name'],'description':s['description'],'provider':{'@id':ORIGIN+'/#business'},'areaServed':{'@type':'Place','name':B['serviceArea']}}
    save('/services/'+s['slug']+'/',s['name']+' Across the Valley',s['description'],content,'/services/',schema)

gallery=intro('Our electrical work','Browse residential, commercial and industrial projects by Montesinos Electric. Select a photo to see it in detail.','Our work')+f'''<section class="page-content wrap"><div class="filters" role="group" aria-label="Filter projects">{''.join(f'<button class="filter" data-filter="{c}" aria-pressed="{str(c=="All").lower()}">{c}</button>' for c in ['All','Residential','Commercial','Industrial'])}<span class="gallery-count" role="status" aria-live="polite">{len(PROJECTS)} projects</span></div><div class="gallery-grid">{''.join(project(p) for p in PROJECTS)}</div></section>'''+cta()
save('/portfolio/','Electrical Project Gallery','View real residential, commercial and industrial projects by Montesinos Electric. Filter photos and explore finished electrical work.',gallery,'/portfolio/')
save('/about/','Our Family-Owned Electrical Business',B['story'],intro('Our family business','Nearly 20 years of electrical experience, with honest pricing and clear communication.','Our story')+story()+f'<section class="section area"><div class="wrap detail-grid"><div><h2>The good guy price.</h2></div><div><p>We offer competitive pricing and explain the work involved in your project. Call us with your plans or the electrical problem you need help with.</p><p style="margin-top:20px">Our projects include new home wiring, commercial lighting and industrial equipment installations.</p><div style="margin-top:26px">{textlink("See what we’ve worked on","/portfolio/")}</div></div></div></section>'+cta(),'/about/')
save('/blog/','Project Stories & Blog','Read residential, commercial and industrial project stories from Montesinos Electric’s existing blog.',intro('Project stories','Photos of our electrical installations for homes, businesses and industrial spaces.','Blog')+f'<section class="page-content wrap"><div class="journal-grid">{"".join(blogcard(p) for p in POSTS)}</div></section>'+cta(),'/blog/')
for post in POSTS:
    slug,category,title,desc=post
    photos=[p for p in PROJECTS if p['category']==category]
    featured={'Residential':PROJECTS[1],'Commercial':PROJECTS[7],'Industrial':PROJECTS[13]}[category]
    content=f'''<section class="page-intro"><div class="wrap"><div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/blog/">Blog</a><span>/</span>{category}</div><div class="article-header"><div><p class="date"><time datetime="2025-10-29">October 29, 2025</time> &nbsp; · &nbsp; Montesinos Electric</p><h1>{category} projects</h1><p>{desc}</p></div>{photo(featured['image'],featured['title'],eager=True)}</div></div></section><section class="article-body"><div class="wrap"><p>View the photos below for examples of our {category.lower()} electrical work.</p><div class="article-gallery">{''.join(project(p) for p in photos)}</div><div style="margin-top:40px">{textlink('Back to all project stories','/blog/')}</div></div></section>'''+cta()
    schema={'@context':'https://schema.org','@type':'BlogPosting','headline':category+' project stories','datePublished':'2025-10-29','author':{'@type':'Organization','name':B['name']},'image':ORIGIN+'/assets/'+Path(featured['image']).with_suffix('.webp').name,'publisher':{'@id':ORIGIN+'/#business'}}
    save('/post/'+slug+'/',category+' Electrical Projects',desc,content,'/blog/',schema)

contact=quote_section()+area()
save('/contact/','Contact & Free Electrical Quote','Contact Montesinos Electric for electrical work across the Valley at (623) 202-2164. Prepare your electrical project details and call for a free quote.',contact)
save('/service-area/','Valley Electrical Service Area','Montesinos Electric serves electrical projects across the Valley. Explore the area map and call to confirm availability for your location.',intro('Valley service area','We work on residential, commercial and industrial electrical projects. Call to confirm availability at your location.','Service area')+area()+cta())
privacy=intro('Website privacy.','How this website handles the details you enter.','Website privacy')+f'''<section class="page-content wrap"><div class="plain-copy"><p>Last updated October 9, 2026.</p><h2>Preparing a quote request</h2><p>The quote form prepares a summary in your browser. It does not send a request, email the business, or save your details to a database. The website does not use local storage to save form entries. The form includes a name, phone number, optional email, project location, service, and project description. You choose whether to copy those details and share them with the team.</p><h2>Calling or copying your details</h2><p>Phone links open your device’s calling application. The copy button writes the prepared request to your clipboard when you select it. Your device or browser may have its own clipboard and autofill settings.</p><h2>Maps and external links</h2><p>Google Maps loads automatically on pages that display the Valley map. Google then handles that map connection under its own <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">privacy policy</a>. The Google Maps business listing also opens on Google’s website. Website hosting may process ordinary connection information to serve pages.</p><h2>Contact</h2><p>For questions about Montesinos Electric, call <a href="tel:{B['phoneLink']}">{B['phone']}</a>.</p></div></section>'''
save('/privacy/','Website Privacy','How the Montesinos Electric redesign handles quote preparation, copying, phone links and maps.',privacy)
access=intro('A website you can use.','If something gets in your way, we want to know.','Accessibility')+f'''<section class="page-content wrap"><div class="plain-copy"><h2>Using this website</h2><p>The website includes keyboard navigation, a skip-to-content link, labelled form fields, text descriptions for project images, visible focus indicators, and layouts that adapt to smaller screens. Project photos open in a dialog that you can close with Escape. Use the arrow keys to move between photos.</p><h2>Photo motion</h2><p>The electrical service photos and the photos in the family-owned business section move gently as you scroll. If your device is set to reduce motion, the photos stay still.</p><h2>Need help?</h2><p>Call <a href="tel:{B['phoneLink']}">{B['phone']}</a> if you need help accessing project information or discussing a quote. Hablamos español.</p><h2>Third-party maps</h2><p>The embedded Google map is provided by Google. You can also use the <a href="{B['mapsUrl']}">Google Maps business listing</a> or call us to discuss your project location.</p></div></section>'''
save('/accessibility/','Accessibility','Keyboard navigation, accessible project viewing and contact help on the Montesinos Electric website.',access)

save('/404/','Page Not Found','Find Montesinos Electric services, project photos and free quotes.',f'<section class="not-found wrap"><h1>Let’s get you<br>back on track.</h1><p>That page could not be found. Explore our services or contact the team.</p>{button("Back to the homepage","/")}</section>')
shutil.copy2(DIST/'404'/'index.html',DIST/'404.html')
# Preserve entry points visitors may follow from the original website.
aliases={'/book-online/':'/services/','/booking-form/':'/contact/','/blank/':'/privacy/','/blank-1/':'/accessibility/'}
for s in SERVICES:
    aliases['/service-page/'+s['slug']+'/']='/services/'+s['slug']+'/'
    aliases['/booking-calendar/'+s['slug']+'/']='/contact/?service='+s['slug']
for path,target in aliases.items():
    f=DIST/path.strip('/')/'index.html';f.parent.mkdir(parents=True,exist_ok=True)
    f.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={target}"><title>Montesinos Electric</title></head><body><p><a href="{target}">Continue to Montesinos Electric</a></p></body></html>',encoding='utf-8')
(DIST/'robots.txt').write_text('User-agent: *\nDisallow: /\n# Private redesign preview. Enable indexing after production launch.\n',encoding='utf-8')
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN+path}</loc></url>' for path in PAGES if path!='/404/')+'</urlset>',encoding='utf-8')
manifest=json.loads((ROOT/'.openai'/'hosting.json').read_text(encoding='utf-8'));manifest['static']={'directory':'dist'}
(ROOT/'.openai'/'hosting.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(ROOT/'page-inventory.json').write_text(json.dumps(PAGES,indent=2),encoding='utf-8')
print(f'Generated {len(PAGES)} pages, {len(aliases)} original URL redirects, and {len(PROJECTS)} project entries.')
