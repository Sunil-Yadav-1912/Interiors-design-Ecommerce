// Get the error message from the URL query parameter
const params = new URLSearchParams(window.location.search);
const errorMessage = params.get('message');

// Display the error message on the page
const errorMessageElement = document.getElementById('error-message');
errorMessageElement.textContent = errorMessage;
