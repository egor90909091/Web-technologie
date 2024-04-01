$(document).ready(function() {
    // Загрузка содержимого страницы при загрузке документа
    $('#content').load('about.html');

    // Обработчик клика на элементы навигации
    $('nav a').click(function(e) {
        e.preventDefault(); // Предотвращаем переход по ссылке

        var pageUrl = $(this).attr('href'); // Получаем URL страницы

        // Загружаем содержимое страницы в блок #content
        $('#content').load(pageUrl);
    });
});
