document.addEventListener("DOMContentLoaded", () => {
    fetch("http://localhost:5001/products")
        .then(response => response.json())
        .then(products => {
            const content = document.getElementById("content");
            products.forEach(product => {
                const div = document.createElement("div");
                div.classList.add("card", "mb-3");
                div.innerHTML = `
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="card-text">${product.description}</p>
                        <p class="card-text">Price: $${product.price}</p>
                    </div>`;
                content.appendChild(div);
            });
        });
});
