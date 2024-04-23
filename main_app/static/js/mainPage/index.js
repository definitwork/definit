const callbackBtn = document.querySelector(".contacts__form-btn");
const callbackForm = document.querySelector(".contacts__form")

callbackBtn.addEventListener("click", () => {
    const form = document.querySelector(".contacts__form");
    const nameUser = form.querySelector("input[name='name']");
    const phoneUser = form.querySelector("input[name='phone']");
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0]
        .value;
    const data = {
        name_user: nameUser.value,
        phone_number_user: phoneUser.value,
    };
    fetch(`http://127.0.0.1:8000/callback/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                return response.json().then((errorData) => {
                    throw new Error(errorData.message);
                });
            }
        })
        .then((data) => {
            console.log('www');
            nameUser.value = "";
            phoneUser.value = "";
        })
        .catch((error) => {
            console.log('qqq');
        });
});
