$(document).ready(function() {
    $('#myModal').on('show.bs.modal', function () {
        $('body').addClass('stop-scrolling');
        $('.carousel').carousel('pause'); // Останавливаем карусель
        // Сбрасываем значения полей ввода
        $('#inputName').val('');
        $('#inputEmail').val('');
        $('#inputPhone').val('');
    });

    $('#myModal').on('hide.bs.modal', function () {
        $('body').removeClass('stop-scrolling');
        $('.carousel').carousel('cycle'); // Возобновляем карусель
    });

    // Открытие модальной формы при нажатии на кнопку "Подобрать авто"
    $('.btn-custom-purple').click(function(){
        $('#myModal').modal('show');
    });

    // Обработчик события нажатия на кнопку "Подтвердить" в первой форме
    $('#submitBtn').click(function(){
        console.log("Кнопка 'Подтвердить' была нажата");
        confirmData(); // Вызываем функцию подтверждения данных
    });

    // Функция подтверждения данных
    function confirmData() {
        var confirmed = window.confirm("Подтвердите действие");
        if (confirmed) {
            // Здесь можно добавить действия по подтверждению
            alert("Введенные данные подтверждены!");
            $('#myModal').modal('hide'); // Закрываем первую модальную форму
        }
    }
});
