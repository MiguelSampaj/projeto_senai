//esse banquinho de dados vai sair jaja//
const data = [
    {
        title: "lorem",
        description: "lorem ipsum dolor sit amet"
    },
    {
        title: "ipsum",
        description: "lalalalalalalala"
    },
    {
        title: "dolor",
        description: "bebeebbeb"
    },
];
////

const cardContainer = document.querySelector(".card-container");
const searchInput = document.querySelector("#searchInput");

const displayData = data => {
    cardContainer.innerHTML = "";
    data.forEach(e => {
        cardContainer.innerHTML += `
        <div class="card">
            <h3>${e.title}</h3>
            <p>${e.description}</p>
        </div>
        `
    })
}

searchInput.addEventListener("keyup", (e) => {
    const value = e.target.value.trim().toLowerCase();

    if (value === "") {
        cardContainer.innerHTML = "";
        return;
    }

    const search = data.filter(item =>
        item.title.toLowerCase().includes(value)
    );

    displayData(search);
});

window.addEventListener("load", () => {
    cardContainer.innerHTML = "";
});


// ----------requisitando os dados de produtos à API------------

async function searchProduct() {
    const response = await fetch(
        "http://127.0.0.1:8000/admin"
    );

    const product = await response.json();

    console.log(product);
}

searchProduct();

//esse banquinho de dados vai embora jaja tbm
const productList = [
    {
        name: "produto1",
        price: 1240.00,
        image: "imagens/product_images/notebook.png"
    },
    {
        name: "produto2",
        price: 1229.99,
        image: "imagens/product_images/notebook.png"
    },
    {
        name: "produto3",
        price: 999.99,
        image: "imagens/product_images/notebook.png"
    }
];

// -------------representando os produtos no html----------------
// dentro de <div id="product">, cria uma <div class="currentProduct"> e os demais dados a cada item recebido
let productArea = document.getElementById("product")
productList.forEach(product => {
    let card = document.createElement("div");

    card.className = "currentProduct";

    card.innerHTML = `
            <img src=${product.image} alt="Imagem">
            <h3>${product.name}</h3>
            <div class="actions">
            <p>R$${product.price}</p>
            <a href="login.html">
                <button>COMPRAR</button>
            </a>
            </div>
    `;
    productArea.appendChild(card);
})
