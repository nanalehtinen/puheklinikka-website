// Menu: mobile toggle and keyboard-accessible dropdown folders.
(function () {
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('mainnav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  var folders = document.querySelectorAll('#mainnav .folder');
  function closeAll(except) {
    folders.forEach(function (f) {
      if (f !== except) {
        f.classList.remove('open');
        f.querySelector('button').setAttribute('aria-expanded', 'false');
      }
    });
  }
  folders.forEach(function (f) {
    var btn = f.querySelector('button');
    btn.addEventListener('click', function () {
      var open = !f.classList.contains('open');
      closeAll(f);
      f.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    f.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && f.classList.contains('open')) {
        closeAll();
        btn.focus();
      }
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('#mainnav .folder')) closeAll();
  });
})();

// Embedded Google Form: after sending, the short thank-you page shows at the top of the tall frame,
// so scroll back up to it instead of leaving the visitor looking at white space (Nana, 2026-10-11).
(function () {
  document.querySelectorAll('iframe[src*="docs.google.com/forms"]').forEach(function (f) {
    f.addEventListener('load', function () {
      // only when the visitor has scrolled down past the top of the form (e.g. to the submit button)
      if (f.getBoundingClientRect().top < 0) {
        var done = document.querySelector('.form-done');
        if (done) { done.hidden = false; done.scrollIntoView({ block: 'start' }); }
        else f.scrollIntoView({ block: 'start' });
      }
    });
  });
})();
