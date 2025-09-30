const form = document.getElementById("contactForm");
const feedbackModalEl = document.getElementById("feedbackModal");
const feedbackModal = new bootstrap.Modal(feedbackModalEl, {backdrop:'static', keyboard:false});
const modalSpinner = document.getElementById("modalSpinner");
const modalSuccess = document.getElementById("modalSuccess");
const successMessage = document.getElementById("successMessage");

form.addEventListener("submit", function(e){
    e.preventDefault(); // prevent normal POST
    modalSpinner.style.display = "block";
    modalSuccess.style.display = "none";
    feedbackModal.show();

    const formData = new FormData(form);

    fetch("", {
        method: "POST",
        headers: {
            "X-CSRFToken": formData.get("csrfmiddlewaretoken")
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        modalSpinner.style.display = "none";
        if(data.success){
            successMessage.innerText = data.success;
            modalSuccess.style.display = "block";
            form.reset(); // optional: clear form
        } else {
            successMessage.innerText = "Something went wrong. Please try again.";
            modalSuccess.style.display = "block";
        }
    })
    .catch(err => {
        modalSpinner.style.display = "none";
        successMessage.innerText = "Error sending message";
        modalSuccess.style.display = "block";
    });
});

