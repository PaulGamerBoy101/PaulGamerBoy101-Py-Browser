document.getElementById("menu").addEventListener("click", function() {
    let menu = document.getElementById("menu-dropdown");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
});

document.getElementById("bookmark").addEventListener("click", function() {
    let url = document.getElementById("url-bar").value;
    saveBookmark(url);
});

function saveBookmark(url) {
    let bookmarks = JSON.parse(localStorage.getItem("bookmarks")) || [];
    if (!bookmarks.includes(url)) {
        bookmarks.push(url);
        localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
    }
}
