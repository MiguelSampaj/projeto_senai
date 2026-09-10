class MenuNavbar {
    constructor(logoMenu, navList, navLinks) {
        this.logoMenu = document.querySelector(logoMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active";

        this.handleClick = this.handleClick.bind(this);
    }

    animateLinks() {
        this.navLinks.forEach((link) => {
            link.style.animation
            ? (link.style.animation = "")
            : (link.style.animation = 'navLinkFade 0.5s ease forwards');
        })
    }

    handleClick() {
        this.navList.classList.toggle(this.activeClass);
        this.animateLinks();
    }
    addClickEvent() {
        this.logoMenu.addEventListener("click", this.handleClick);
    }
    
    init() {
        if (this.logoMenu) {
            this.addClickEvent();
        }
        return this;
    }
}

const menuNavbar = new MenuNavbar(
    ".logo-menu",
    ".nav-list",
    ".nav-list li",
);
menuNavbar.init();
