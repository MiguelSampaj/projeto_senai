//dados//
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


const productList = [
    {
        name: "sla1",
        price: 1244,
        image: "imagens/product_images/notebook.png"
    },

    {
        name: "sla2",
        price: 1244,
        image: "imagens/product_images/notebook.png"
    },

    {
        name: "sla3",
        price: 99399,
        image: "imagens/product_images/notebook.png"
    }
];


let productArea = document.getElementById("product")

productList.forEach(product => {

    let card = document.createElement("div");

    card.className = "currentProduct";

    card.innerHTML = `
            <img src=${product.image} alt="notebook">
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