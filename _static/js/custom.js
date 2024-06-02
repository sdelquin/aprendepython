document.addEventListener("DOMContentLoaded", (event) => {
  // https://github.com/pradyunsg/furo/issues/28#issuecomment-1380549435
  document.body.setAttribute("data-theme", "light");

  // Button to hide mobile menu -> Zen mode for presentations
  const hideMenuButton = document.createElement("label");
  hideMenuButton.innerHTML = '<img src="/_static/img/hide-item.svg">';
  hideMenuButton.classList.add("nav-overlay-icon");
  hideMenuButton.id = "btn-hide-menu";
  hideMenuButton.addEventListener("click", function (event) {
    document.querySelector(".mobile-header").style.display = "none";
  });
  document
    .querySelector(".mobile-header .header-left")
    .appendChild(hideMenuButton);

  // Dynamic TOC (Gumshoe)
  // https://github.com/cferdinandi/gumshoe#nested-navigation
  // https://github.com/pradyunsg/furo/blob/main/src/furo/assets/scripts/furo.js#L141
  new Gumshoe(".toc-tree a", {
    reflow: true,
    recursive: true,
    navClass: "scroll-current",
    nested: true,
    nestedClass: "scroll-current",
    offset: () => {
      let offset = 10;
      const header = document.querySelector("header.mobile-header");
      if (header != null) {
        offset += header.offsetHeight;
      }
      return offset;
    },
  });
});
