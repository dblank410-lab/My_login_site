const form = document.getElementById("loginForm");

form.addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        username: form.username.value,
        password: form.password.value
    };

    try {
        const res = await fetch("/send-email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        alert(result.message);
    } catch (err) {
        console.error(err);
        alert("Error sending email");
    }
});
