 function toggleMenu() {
  const nav = document.querySelector(".nav-content nav");
  nav.classList.toggle("active");
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    const countSpan = document.getElementById('cartCount');
    if (countSpan) {
      countSpan.textContent = totalItems;
      countSpan.style.display = totalItems > 0 ? 'inline-block' : 'none';
    }
  }

  // Call on page load
  updateCartCount();

  // ✅ Listen for updates from other tabs/windows/pages
  window.addEventListener('storage', function (e) {
    if (e.key === 'cart') {
      updateCartCount();
    }
  });

  // ✅ Listen for custom event to trigger update without page refresh
  window.addEventListener('cartUpdated', updateCartCount);

  
  // ✅ Cart function with login restriction
window.addToCart = function (product) {
  const loggedInUser = JSON.parse(localStorage.getItem('loggedInUser'));

  if (!loggedInUser) {
    alert("Please log in to add items to the cart.");
    window.location.href = "login.html"; // Redirect to login/registration page
    return;
  }

  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  const existing = cart.find(item => item.name === product.name);
  if (existing) {
    existing.quantity += 1;
  } else {
    product.quantity = 1;
    cart.push(product);
  }

  localStorage.setItem('cart', JSON.stringify(cart));
  alert(`${product.name} added to cart!`);

  // Dispatch event to update cart count on all pages
  window.dispatchEvent(new Event('cartUpdated'));
};

