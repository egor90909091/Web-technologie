function submitCarForm() {
    // Получение данных из формы
    var make = document.getElementById("make").value;
    var model = document.getElementById("model").value;
    var year = document.getElementById("year").value;
    var color = document.getElementById("color").value;

    // Вывод данных в модальном окне
    var modalContent = "Марка: " + make + "<br>";
    modalContent += "Модель: " + model + "<br>";
    modalContent += "Год выпуска: " + year + "<br>";
    modalContent += "Цвет: " + color + "<br>";

    document.getElementById("myModal").getElementsByClassName("modal-body")[0].innerHTML = modalContent;
}
