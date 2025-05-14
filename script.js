// Initialize orders and products
const orderCount = document.getElementById("orderCount");
const orderList = document.getElementById("orderList");
const orders = JSON.parse(localStorage.getItem("orders") || "[]");
const products = JSON.parse(localStorage.getItem("products") || "[]");

orderCount.textContent = orders.length;

// Show orders
orders.forEach((order, i) => {
  const div = document.createElement("div");
  div.className = "order";
  div.innerHTML = `<strong>Order #${i + 1}</strong><br>${JSON.stringify(order)}`;
  orderList.appendChild(div);
});

// Add Product
document.getElementById("addProductForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const reader = new FileReader();
  const file = document.getElementById("image").files[0];

  reader.onload = function() {
    const id = Date.now().toString();
    const newProduct = {
      id,
      name: document.getElementById("name").value,
      price: document.getElementById("price").value,
      description: document.getElementById("description").value,
      image: reader.result
    };

    products.push(newProduct);
    localStorage.setItem("products", JSON.stringify(products));

    alert("Product added!");
    window.open(`product.html?id=${id}`, "_blank");
    document.getElementById("addProductForm").reset();
  };

  reader.readAsDataURL(file);
});
