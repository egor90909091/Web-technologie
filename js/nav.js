// nav.js

// Получаем текущий URL страницы
var url = window.location.href;

// Перебираем все ссылки в навигации
document.querySelectorAll('.navbar-nav a').forEach(function(element) {
    // Если URL ссылки совпадает с текущим URL страницы
    if (element.href === url) {
        // Добавляем класс active к найденному элементу
        element.classList.add('active');
    }
});
