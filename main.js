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