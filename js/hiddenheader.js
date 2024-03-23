document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.accordion-header');

    headers.forEach(header => {
        header.addEventListener('click', function() {
            const content = this.nextElementSibling;
            content.classList.toggle('accordion-content-active');

            if (content.classList.contains('accordion-content-active')) {
                content.style.maxHeight = content.scrollHeight + 'px';
                this.style.background = '#dc3545'; // изменение фона заголовка при раскрытии
            } else {
                content.style.maxHeight = 0;
                this.style.background = ''; // сброс фона заголовка при сворачивании
            }
        });
    });
});
