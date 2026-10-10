(() => {
  // Each photo owns its motion; the fixed frames and surrounding text stay put.
  // The page remains complete when either vendor script is unavailable.
  if (!window.gsap || !window.ScrollTrigger) return;
  const { gsap, ScrollTrigger } = window;
  gsap.registerPlugin(ScrollTrigger);

  gsap.matchMedia().add({
    desktop: '(min-width: 768px)',
    mobile: '(max-width: 767px)',
    reduce: '(prefers-reduced-motion: reduce)'
  }, context => {
    if (context.conditions.reduce) return;
    const mobile = context.conditions.mobile;
    const travel = mobile ? 32 : 72;
    const bleed = mobile ? 48 : 96;

    document.querySelectorAll('.photo-frame').forEach((frame, index) => {
      const img = frame.querySelector('img');
      if (!img) return;
      gsap.set(frame, { '--photo-bleed': `${bleed}px` });
      gsap.fromTo(img,
        { y: -travel, scale: 1.12 },
        { y: travel, scale: 1, ease: 'none', scrollTrigger: {
          id: `photo-drift-${index}`, trigger: frame,
          start: 'clamp(top bottom)', end: 'clamp(bottom top)',
          scrub: 0.45, invalidateOnRefresh: true
        } }
      );

      // The opening photo starts fully visible. Other photos reveal their
      // lower edge as they enter, and rewind when the visitor scrolls back.
      if (!frame.classList.contains('hero-photo')) {
        gsap.fromTo(frame,
          { clipPath: 'inset(0% 0% 18% 0%)' },
          { clipPath: 'inset(0% 0% 0% 0%)', ease: 'none', scrollTrigger: {
            id: `photo-reveal-${index}`, trigger: frame,
            start: 'top 94%', end: 'top 60%',
            scrub: 0.3, invalidateOnRefresh: true
          } }
        );
      }
    });
    // matchMedia automatically reverts these styles and triggers on resize
    // and when the motion preference changes. No hidden content is required.
  });

  document.fonts?.ready.then(() => ScrollTrigger.refresh());
  window.addEventListener('load', () => ScrollTrigger.refresh(), { once: true });

  document.querySelector('.hero-down')?.addEventListener('click', event => {
    // Preserve native instant anchor navigation for keyboard users.
    if (!event.detail || event.ctrlKey || event.metaKey || event.shiftKey ||
        window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const section = document.querySelector('#electrical-services');
    if (!section) return;
    event.preventDefault();
    section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    section.focus({ preventScroll: true });
  });
})();
