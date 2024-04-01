// table-sort.js

let sortOrder = 1;

function sortTable() {
    const table = document.getElementById('priceTable');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((rowA, rowB) => {
        const priceA = getPrice(rowA.cells[1].textContent);
        const priceB = getPrice(rowB.cells[1].textContent);

        return sortOrder * (priceA - priceB);
    });

    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));

    // Переключаем направление сортировки
    sortOrder *= -1;
}

function getPrice(priceString) {
    const price = priceString.replace(/\D/g, ''); // удаляем все символы, кроме цифр
    return parseInt(price);
}
