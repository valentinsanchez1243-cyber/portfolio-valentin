const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = 1;
      entry.target.style.transform = "translateY(0)";
      // Optionally stop observing after reveal
      // revealObserver.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.12,
  rootMargin: "0px 0px -50px 0px"
});

document.querySelectorAll('.section').forEach((section) => {
  section.style.opacity = 0;
  section.style.transform = "translateY(50px)";
  section.style.transition = "all 0.8s cubic-bezier(.16,1,.3,1)";
  revealObserver.observe(section);
});

// Cursor follow
const cursor = document.getElementById('cursor');
if (cursor) {
  document.addEventListener('mousemove', e => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
  });
}

// Video auto-play on hover for specific grids
document.querySelectorAll('video').forEach(video => {
  if (video.hasAttribute('muted') && !video.hasAttribute('controls')) {
    video.addEventListener('mouseenter', () => video.play());
    video.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = 0;
    });
  }
});

// Menu logic
const movl = document.getElementById('movl');
const mtog = document.getElementById('mtog');
if (movl && mtog) {
  mtog.addEventListener('click', () => {
    movl.classList.toggle('active');
    mtog.classList.toggle('active');
  });
}
