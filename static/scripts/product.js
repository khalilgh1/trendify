// Quantity control functionality
console.log('Product script loaded');
const quantityInput = document.getElementById('quantityInput');
const decreaseBtn = document.getElementById('decreaseBtn');
const increaseBtn = document.getElementById('increaseBtn');
const totalPriceElement = document.getElementById('totalPrice');
const unitPriceElement = document.getElementById('unitPrice');
const deliveryTaxElement = document.getElementById('deliveryTax');
const wilayaSelect = document.querySelector('.wilaya-select');
const deliverySelect = document.querySelector('.delivery-select');

const data = JSON.parse(document.getElementById("data-json").textContent);
console.log(data);

wilaya = null;
DELIVERY_TAX = 0;
const UNIT_PRICE = unitPriceElement.dataset.unitPrice? parseInt(unitPriceElement.dataset.unitPrice) : 0;

//ensure delivery select is disabled initially
wilayaSelect.addEventListener('change', function () {
    const selectedWilaya = this.value; 
    if (selectedWilaya) {
        wilaya = selectedWilaya;
        console.log(`Selected Wilaya: ${wilaya}`);
        deliverySelect.disabled = false;
        // reset delivery select options
        deliverySelect.value = '';
        DELIVERY_TAX = 0;
        //disable office option for wilayas that do not have office delivery
        Object.values(data).forEach(function (val) {
            if (val.wilaya === wilaya) {
                const officeDelivery = val.office;
                if (officeDelivery && !isNaN(officeDelivery)) {
                    deliverySelect.querySelector('.office-option').disabled = false;
                }
                else {
                    deliverySelect.querySelector('.office-option').disabled = true;
                }
            }
        });

    }
    else{
        wilaya = null;
        deliverySelect.disabled = true;
        // reset delivery select options
        deliverySelect.value = '';
        DELIVERY_TAX = 0;
    }
    updateTotal();

});
//update delivery select options based on wilaya
deliverySelect.addEventListener('change', function () {
    const selectedDelivery = this.value;
    if (selectedDelivery) {
        console.log(`Selected Delivery Type: ${selectedDelivery}`);
        // You can add additional logic here based on the selected delivery type
        //extract the data attribute from the selected option
        const selectedWilayaOption = wilayaSelect.options[wilayaSelect.selectedIndex];
        const homeDelivery = selectedWilayaOption.dataset.home;
        const officeDelivery = selectedWilayaOption.dataset.office;
        if (selectedDelivery === 'home' && homeDelivery) {
            DELIVERY_TAX = parseInt(homeDelivery);
            deliveryTaxElement.textContent = `${DELIVERY_TAX}DA`;
        } else if (selectedDelivery === 'office' && officeDelivery) {
            DELIVERY_TAX = parseInt(officeDelivery);
            deliveryTaxElement.textContent = `${DELIVERY_TAX}DA`;
        } else {
            DELIVERY_TAX = 0;
            deliveryTaxElement.textContent = '0DA';
        }
        updateTotal();

    }
    else{
        console.log('No delivery type selected');
    }
});


function updateTotal() {
    deliveryTaxElement.textContent = `${DELIVERY_TAX}DA`;
    const quantity = parseInt(quantityInput.value) || 1;
    const total = (UNIT_PRICE * quantity) + DELIVERY_TAX;
    totalPriceElement.textContent = `${total}DA`;

    // Update unit price display
    unitPriceElement.textContent = `${UNIT_PRICE * quantity}DA`;
}

// Decrease quantity
decreaseBtn.addEventListener('click', function () {
    let currentValue = parseInt(quantityInput.value) || 1;
    if (currentValue > 1) {
        quantityInput.value = currentValue - 1;
        updateTotal();
    }
});

// Increase quantity
increaseBtn.addEventListener('click', function () {
    let currentValue = parseInt(quantityInput.value) || 1;
    if (currentValue < 99) {
        quantityInput.value = currentValue + 1;
        updateTotal();
    }
});

// Handle manual input
quantityInput.addEventListener('input', function () {
    let value = parseInt(this.value);
    if (isNaN(value) || value < 1) {
        this.value = 1;
    } else if (value > 99) {
        this.value = 99;
    }
    updateTotal();
});

// Prevent non-numeric input
quantityInput.addEventListener('keypress', function (e) {
    if (!/^\d$/.test(e.key) && !['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'].includes(e.key)) {
        e.preventDefault();
    }
});

// Form submission
const form = document.getElementById('customerForm');

form.addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent default submission initially

    // Get form data
    const fullName = this.querySelector('.name-input').value;
    const phone = this.querySelector('.phone-input').value;
    const wilaya = this.querySelectorAll('select')[0].value;
    const deliveryType = this.querySelectorAll('select')[1].value;
    const address = this.querySelector('textarea').value;
    const quantity = quantityInput.value;
    const buyButton = document.querySelector('.buy-button');
    const originalText = buyButton.textContent;
    const processingText = buyButton.dataset.processingText;
    const orderedText = buyButton.dataset.orderedText;

    // Hidden inputs for form submission
    const unitPriceInput = document.querySelector('.unit-price-input');
    const deliveryTaxInput = document.querySelector('.delivery-tax-input');
    const totalPriceInput = document.querySelector('.total-price-input');

    // Elements used to get display values
    const deliveryTaxElement = document.getElementById('deliveryTax');
    const totalPriceElement = document.getElementById('totalPrice');

    // Validate required fields
    if (!fullName || !phone || !wilaya || !deliveryType || !address) {
        alert('Please fill in all required fields');
        return;
    }

    // Update the values on the hidden inputs before submission
    unitPriceInput.value = UNIT_PRICE;
    deliveryTaxInput.value = deliveryTaxElement.textContent.replace('DA', '').trim();
    totalPriceInput.value = totalPriceElement.textContent.replace('DA', '').trim();

    // Debug log
    console.log('Order submitted:', {
        fullName,
        phone,
        wilaya,
        deliveryType,
        address,
        quantity,
        unitPrice: unitPriceInput.value,
        deliveryTax: deliveryTaxInput.value,
        totalPrice: totalPriceInput.value
    });

    // Simulate order processing
    buyButton.textContent = processingText;
    buyButton.disabled = true;
    buyButton.style.background = 'linear-gradient(135deg, #6c757d, #495057)';

    setTimeout(() => {
        buyButton.textContent = orderedText;
        buyButton.style.background = 'linear-gradient(135deg, #28a745, #20c997)';

        setTimeout(() => {
            buyButton.textContent = originalText;
            buyButton.disabled = false;
            buyButton.style.background = 'linear-gradient(135deg, #ff8a50, #ff6b35)';

            // Reset form
            form.reset();
            quantityInput.value = 1;
            updateTotal();
        }, 2000);
    }, 1500);

    // Submit the form manually with updated fields
    form.submit();
});


// Enhanced form interactions
const inputs = document.querySelectorAll('.form-input, .form-select, .form-textarea');
inputs.forEach(input => {
    input.addEventListener('focus', function () {
        this.parentElement.style.transform = 'translateY(-1px)';
    });

    input.addEventListener('blur', function () {
        this.parentElement.style.transform = 'translateY(0)';
    });
});

// Initialize total price
updateTotal();

//swiper js
 const swiper = new Swiper(".mySwiper", {
      loop: true,
      autoplay: {
        delay: 3000,
        disableOnInteraction: false,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      effect: "slide", // Change to "fade", "cube", etc.
    });