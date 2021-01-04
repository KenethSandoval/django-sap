const item = document.getElementById('active');

item.addEventListener('click', (e) => {
    e.preventDefault();
    item.classList.add('active');
});
