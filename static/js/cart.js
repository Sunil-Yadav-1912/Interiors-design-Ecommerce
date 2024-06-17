const crossIcons = document.querySelectorAll('.cross-icon');

// Add click event listener to each cross icon
crossIcons.forEach(crossIcon => {
    crossIcon.addEventListener('click', function() {
        // Get the item details from the data attributes of the image
        const itemId = this.dataset.id;
        const itemName = this.dataset.name;
        const itemImage = this.dataset.image;
        const itemPrice = this.dataset.price;

        // Send item details via POST request to your API
        fetch('/add_to_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: itemId,
                name: itemName,
                image: itemImage,
                price: itemPrice
            })
        })
        .then(response => response.json()) // Parse response JSON
        .then(data => {
            // Display response message
            alert(data.message); // You can replace alert with any UI notification method
        })
        .catch(error => {
            // Handle error if needed
            console.error('Error adding item to cart:', error);
        });
    });
});