// Получаем текущий путь страницы
var currentPath = window.location.pathname;

// Получаем все ссылки навигации
var navLinks = document.querySelectorAll('.navbar-nav a');

// Перебираем все ссылки навигации
navLinks.forEach(function(link) {
    // Получаем путь ссылки
    var linkPath = link.getAttribute('href');
    
    // Сравниваем пути ссылки и текущей страницы
    if (linkPath === currentPath) {
        // Если пути совпадают, добавляем класс активности
        link.classList.add('active');
    }
});
