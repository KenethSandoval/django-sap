let settings = document.getElementById('settings');
let newsettings = document.getElementById('newsettings');

settings.addEventListener('mouseover', () => {
    newsettings.classList.add('fa-spin');
    newsettings.style.transitionDelay="0.6s"
});

settings.addEventListener('mouseout', () => {
    newsettings.classList.remove('fa-spin');
    newsettings.style.transitionDelay="0.6s"
});
