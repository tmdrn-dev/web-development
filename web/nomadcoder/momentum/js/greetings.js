const loginForm = document.querySelector("#login-form")
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const CLASS_HIDDEN = "hidden";
const LS_KEY_USERNAME = "username";

function showGreeting(username) {
    greeting.innerText = `Hello ${username}!`;
    greeting.classList.remove(CLASS_HIDDEN);
}

function onLoginSubmit(event) {
    event.preventDefault(); // block to submit form
    
    loginForm.classList.add(CLASS_HIDDEN);
    
    const username = loginInput.value;
    localStorage.setItem(LS_KEY_USERNAME, username);
    
    showGreeting(username);
}

const savedUsername = localStorage.getItem(LS_KEY_USERNAME);
if (savedUsername === null) {
    // show login form
    loginForm.classList.remove(CLASS_HIDDEN);
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    // show greeting
    showGreeting(savedUsername);
}
