

let number_of_reviews=20;
let number_of_rating_recived=17;
let percentage = (number_of_rating_recived/number_of_reviews)*100;
let not_p=100 -percentage;




// Get all the rating cards, set event listeners on them to handle mouseover, mouseout, and click events, and submit form data
let cards = document.querySelectorAll('.rating');
let form = document.querySelector('#myForm');
let reviewCards = document.getElementById('review-cards');

// Iterate over each rating card and set event listeners on each star icon within the card
cards.forEach(card => {
let starIcons = card.querySelectorAll('.bi');
let selectedRating = 0;



    starIcons.forEach((starIcon, index) => {
        starIcon.addEventListener('mouseover', () => {
            for (let i = 0; i <= index; i++) {
                starIcons[i].classList.remove('bi-star');
                starIcons[i].classList.add('bi-star-fill');
            }
        });

        starIcon.addEventListener('mouseout', () => {
            for (let i = 0; i <= index; i++) {
                if (i >= selectedRating) {
                    starIcons[i].classList.remove('bi-star-fill');
                    starIcons[i].classList.add('bi-star');
                }
            }
        });

        starIcon.addEventListener('click', () => {
            if (selectedRating === index + 1) {
                selectedRating = 0; // Deselect the rating
              } else {
                selectedRating = index + 1; // Select the rating
              }
        });
    });

});


