console.log("Home script loaded");
// Search functionality
const searchInput = document.querySelector('.search-input');
const productCards = document.querySelectorAll('.product-card');
const searchForm = document.querySelector('.search-container');


// Add to cart functionality
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function (e) {
        e.stopPropagation();
        id = e.target.dataset.productId;
        window.location.href = `/product/${id}`;
    });
});
//"add a new product" functionality
//just redirect to the product creation page
document.querySelector('.add-product').addEventListener('click', function () {
    window.location.href = '/add-product';
}
);
// "edit product" functionality
document.querySelectorAll('.edit-product').forEach(button => {
    button.addEventListener('click', function (e) {
        e.stopPropagation();
        const id = e.target.dataset.productId;
        window.location.href = `/edit-product/${id}`;
    });
});
// "delete product" functionality
// just redirect to the product deletion page
document.querySelectorAll('.delete-product').forEach(button => {
    button.addEventListener('click', function (e) {
        e.stopPropagation();
        const id = e.target.dataset.productId;
        window.location.href = `/delete-product/${id}`;
    });
}
);


// Product card click functionality
productCards.forEach(card => {
    card.addEventListener('click', function () {
        const productName = this.querySelector('.product-name').textContent;
        console.log(`Viewing product: ${productName}`);
        // Here you would typically navigate to product detail page
    });
});

// Simple notification system
function showNotification(message) {
    const notification = document.createElement('div');
    notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: linear-gradient(135deg, #28a745, #20c997);
                color: white;
                padding: 1rem 2rem;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
                z-index: 10000;
                animation: slideIn 0.3s ease;
            `;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideIn 0.3s ease reverse';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Enhanced search with categories
searchInput.addEventListener('focus', function () {
    prevText = searchInput.placeholder;
    this.placeholder = '';
});
searchInput.addEventListener('blur', function () {
    this.placeholder = prevText;
});



// Intersection Observer for animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animationPlayState = 'running';
        }
    });
});

productCards.forEach(card => {
    observer.observe(card);
});