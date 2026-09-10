// ----------Requisitando os dados à API------------
async function searchProduct() {
    const response = await fetch(
        "http://127.0.0.1:8000/api/products/"
    );

    const productList = await response.json();

    console.log(productList);

    /*MOSTRANDO OS PRODUTOS NO HTML
        seleciona o elemento de id 'product'.
        dentro de <div id="product">, cria uma <div class="currentProduct"> a cada item recebido
        adiciona na div os dados recebidos
    */
    let productArea = document.getElementById("product");

    productList.forEach(product => {

        let card = document.createElement("div");

        card.className = "currentProduct";

        card.innerHTML = `
            <img src="${product.product_image}" alt="Imagem">
            <h3>${product.product_name}</h3>
            <div class="actions">
                <p>R$${product.product_price}</p>
                <a href="login.html">
                    <button>COMPRAR</button>
                </a>
            </div>
        `;
        productArea.appendChild(card);
    })

// ----SEARCHBAR----
    const cardContainer = document.querySelector(".card-container");
    const searchInput = document.querySelector("#searchInput");
    const displayData = productList => {

        cardContainer.innerHTML = "";
        productList.forEach(product => {
            cardContainer.innerHTML += `
            <div class="card">
                <h3>${product.product_name}</h3>
                <p>${product.product_description}</p>
            </div>
            `
        })
    }

    searchInput.addEventListener("keyup", (product) => {
        const value = product.target.value.trim().toLowerCase();

        if (value === "") {
            cardContainer.innerHTML = "";
            return;
        }

        const search = productList.filter(item =>
            item.product_name.toLowerCase().includes(value)
        );

        displayData(search);
    });

    window.addEventListener("load", () => {
        cardContainer.innerHTML = "";
    });

};
searchProduct();
