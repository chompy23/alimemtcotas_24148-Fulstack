function redireccion(url){
    
    window.location.href =url;
}
document.addEventListener('DOMContentLoaded', () => {
    const decrementButtons = document.querySelectorAll('.decrement');
    const incrementButtons = document.querySelectorAll('.increment');
    const quantityInputs = document.querySelectorAll('.quantity');
    const pricePerItems = document.querySelectorAll('.price-per-item');
    const totalPriceElement = document.getElementById('total-price');
    const buyButton = document.getElementById('buy-button');
    const floatingBar = document.querySelector('.floating-bar');
    
    function updateTotalPrice() {
        let totalPrice = 0;
        quantityInputs.forEach((input, index) => {
            const quantity = parseInt(input.value);
            const pricePerItem = parseFloat(pricePerItems[index].textContent.replace(/[^0-9.-]+/g, ""));
            totalPrice += quantity * pricePerItem;
        });
        totalPriceElement.textContent = totalPrice.toFixed(2);
        toggleFloatingBar(totalPrice);
    }

    function toggleFloatingBar(totalPrice) {
        if (totalPrice > 0) {
            floatingBar.style.display = 'flex';
        } else {
            floatingBar.style.display = 'none';
        }
    }

    decrementButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            let quantity = parseInt(quantityInputs[index].value);
            if (quantity > 0) {
                quantity--;
                quantityInputs[index].value = quantity;
                updateTotalPrice();
            }
        });
    });

    incrementButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            let quantity = parseInt(quantityInputs[index].value);
            quantity++;
            quantityInputs[index].value = quantity;
            updateTotalPrice();
        });
    });

    buyButton.addEventListener('click', () => {
        alert('Gracias por comprar en Alimencotas');
    });

    updateTotalPrice();
    
});