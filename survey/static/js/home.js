function openNav() {
    document.getElementById("myNav").style.width = "30%";
}           
function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}

twemoji.parse(document.body, {
    base: 'https://twemoji.maxcdn.com/v/12.1.4/',
    folder: 'svg',
    ext: '.svg',
    });