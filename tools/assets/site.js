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
  var folders = document.querySelectorAll('.mainnav .folder');
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
    if (!e.target.closest('.mainnav .folder')) closeAll();
  });
})();
