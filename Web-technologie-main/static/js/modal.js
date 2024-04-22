$(document).ready(function () {
    // Обработчик клика на кнопке "Подобрать авто"
    $(document).on('click', '.btn-custom-purple', function () {
        $('#myModal').modal('show'); // Открываем модальное окно
    });

    // Обработчик события отображения модального окна
    $('#myModal').on('show.bs.modal', function () {
        $('body').addClass('stop-scrolling'); // Запрет прокрутки страницы
        $('.carousel').carousel('pause'); // Останавливаем карусель
        // Сбрасываем значения полей ввода
        $('#inputName').val('');
        $('#inputEmail').val('');
        $('#inputPhone').val('');
    });

    // Обработчик события закрытия модального окна
    $('#myModal').on('hide.bs.modal', function () {
        $('body').removeClass('stop-scrolling'); // Возобновляем прокрутку страницы
        $('.carousel').carousel('cycle'); // Возобновляем карусель
    });

    // Обработчик события нажатия на кнопку "Подтвердить" в первой форме
    $(document).on('click', '#submitBtn', function () {
        console.log("Кнопка 'Подтвердить' была нажата");
        confirmData(); // Вызываем функцию подтверждения данных
    });

    // Функция подтверждения данных
    function confirmData() {
        var formData = {
            name: $('#inputName').val(),
            email: $('#inputEmail').val(),
            phone: $('#inputPhone').val()
        };

        $.ajax({
            url: '/submit_form',
            type: 'POST',
            data: formData,
            success: function (response) {
                alert(response); // Отображаем ответ сервера после успешной отправки формы
                $('#myModal').modal('hide'); // Закрываем модальное окно
            },
            error: function (xhr, status, error) {
                console.error(error); // Обработка ошибок при отправке формы
            }
        });
    }
});
