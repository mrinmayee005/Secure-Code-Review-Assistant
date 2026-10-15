// Input_Data/Sample_Code/vulnerable_xss.js
function displayGreeting() {
    const params = new URLSearchParams(window.location.search);
    const user = params.get('name');
    document.getElementById('welcome-banner').innerHTML = "Welcome back, " + user;
}
