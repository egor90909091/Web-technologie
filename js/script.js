function toggleContent(element) {
    // Находим ближайший родительский элемент с классом 'content1'
    var content = $(element).next('.content1');
    
    // Переключаем видимость содержимого
    content.find('img, p').toggleClass('hidden');
}
