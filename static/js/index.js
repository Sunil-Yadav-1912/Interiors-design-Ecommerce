document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        // Retrieve item details from data attributes
        const itemId = this.getAttribute('data-id');
        const itemName = this.getAttribute('data-name');
        const itemImage = this.getAttribute('data-image');
        const itemPrice = this.getAttribute('data-price');

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

document.querySelectorAll('.more-info-btn').forEach(btn => {
 btn.addEventListener('click', function() {
     // Retrieve item details from data attributes
     const itemId = this.getAttribute('data-id');
     const itemName = this.getAttribute('data-name');
     const itemImage = this.getAttribute('data-image');
     const itemPrice = this.getAttribute('data-price');
     const itemDescription = this.getAttribute('data-description');

     // Send item details via POST request to your API
     fetch('/more-info', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify({
             itemId: itemId,
             name: itemName,
             image: itemImage,
             price: itemPrice,
             description: itemDescription
         })
     })
     .then(response => {
         if (!response.ok) {
             throw new Error('Network response was not ok ' + response.statusText);
         }
         return response.text(); // Assuming the response is text/html since we expect a page
     })
     .then(html => {
         // Here, `html` is the HTML returned from your Flask application
         // You can directly write it to your document, or to a particular div
         document.documentElement.innerHTML = html;
     })
     .catch(error => {
         console.error('Error fetching more info:', error);
     });
 });
});

$(document).on('click', '.add-to-cart-inside-btn', function() {
    const itemId = $(this).data('id');
    const itemName = $(this).data('name');
    const itemImage = $(this).data('image');
    const itemPrice = $(this).data('price');

    $.ajax({
        url: '/add_to_cart',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            id: itemId,
            name: itemName,
            image: itemImage,
            price: itemPrice
        }),
        success: function(data) {
            alert(data.message);
        },
        error: function(xhr, status, error) {
            console.error('Error adding item to cart:', error);
        }
    });
});

   function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

//   $(document).ready(function(){
//     $(".fashion-carousel").owlCarousel({
//        items: 3,
//        loop: false, // Disable looping
//        margin: 20,
//        autoplay: false, // Disable autoplay
//        autoplayTimeout: 3000,
//        autoplayHoverPause: false, // Disable pause on hover
//        responsive:{
//           0:{
//              items:1
//           },
//           600:{
//              items:2
//           },
//           1000:{
//              items:3
//           }
//        }
//     });
 
//     $(".scroll-left-btn").click(function() {
//        var carousel = $(this).parent().siblings('.fashion-carousel');
//        carousel.trigger('prev.owl.carousel');
//     });
 
//     $(".scroll-right-btn").click(function() {
//        var carousel = $(this).parent().siblings('.fashion-carousel');
//        carousel.trigger('next.owl.carousel');
//     });
//  });
 
$(document).ready(function(){
    $(".scroll-left-btn").click(function() {
       $("#main_slider").carousel("prev");
    });
 
    $(".scroll-right-btn").click(function() {
       $("#main_slider").carousel("next");
    });
 });