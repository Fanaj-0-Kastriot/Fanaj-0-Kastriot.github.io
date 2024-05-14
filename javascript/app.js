document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    alert("Inscription réussie !");
});
