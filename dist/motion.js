(() => {
  // Service and family-business photos drift inside still frames; copy stays put.
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
    const travel = mobile ? 9 : 18;
    const bleed = mobile ? 16 : 28;

    document.querySelectorAll('.service-thumb .photo-frame, .story-photos .photo-frame').forEach((frame, index) => {
      const img = frame.querySelector('img');
      if (!img) return;
      gsap.set(frame, { '--photo-bleed': `${bleed}px` });
      gsap.fromTo(img,
        { y: -travel },
        { y: travel, ease: 'none', scrollTrigger: {
          id: `photo-drift-${index}`, trigger: frame,
          start: 'clamp(top bottom)', end: 'clamp(bottom top)',
          scrub: 1.2, invalidateOnRefresh: true
        } }
      );
    });
    // matchMedia automatically reverts these styles and triggers on resize
    // and when the motion preference changes. No hidden content is required.
  });

  document.fonts?.ready.then(() => ScrollTrigger.refresh());
  window.addEventListener('load', () => ScrollTrigger.refresh(), { once: true });

})();
