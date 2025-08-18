document.getElementById("checkStatusBtn").addEventListener("click", function() {
    const message = document.getElementById("statusMessage");
    const num = parseInt(prompt("Enter a number:"));

    if (num % 2 === 0) {
        message.textContent = num + " is Even.";
        message.style.color = "green";
    } else {
        message.textContent = num + " is Odd.";
        message.style.color = "crimson";
    }
});