function addItem() {
    const container = document.getElementById('items-container');

    const div = document.createElement('div');
    div.classList.add('item-row');

    const itemSelect = document.createElement('select');
    itemSelect.name = "item[]";
    for (let key in products) {
        const opt = document.createElement('option');
        opt.value = key;
        opt.innerText = key;
        itemSelect.appendChild(opt);
    }

    const quantitySelect = document.createElement('select');
    quantitySelect.name = "quantity[]";
    for (let i = 1; i <= 50; i++) {
        const opt = document.createElement('option');
        opt.value = i;
        opt.innerText = i;
        quantitySelect.appendChild(opt);
    }

    div.appendChild(itemSelect);
    div.appendChild(quantitySelect);
    container.appendChild(div);
}
