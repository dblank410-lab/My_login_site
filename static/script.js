// static/script.js

const form = document.getElementById("loginForm");

form.addEventListener("submit", function(e){

    e.preventDefault();

    alert(
        "Educational demo only.\nNever enter real passwords into unknown websites."
    );

});