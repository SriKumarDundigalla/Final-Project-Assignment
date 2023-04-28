// graphs
// Get the canvas element and set the initial data for the chart
let ctx = document.getElementById('myratingChart');
let number_of_reviews=20;
let number_of_rating_recived=17;
let percentage = (number_of_rating_recived/number_of_reviews)*100;
let not_p=100 -percentage;

// Create a new doughnut chart using Chart.js library
new Chart(ctx, {
type: 'doughnut',
data: {
labels: [
    'satisfied','Unsatisfied'
],
datasets: [{
label: 'Over all user review based on star rating',
data: [percentage, not_p],
backgroundColor: [
'rgb(54, 162, 235)',
'rgb(255, 99, 132)',
],
hoverOffset: 4
}]
},
options: {
responsive: true
}
});

// Get all the rating cards, set event listeners on them to handle mouseover, mouseout, and click events, and submit form data
let cards = document.querySelectorAll('.rating');
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
    form.addEventListener('submit', (event) => {
        
        event.preventDefault(); 
        // update chart data
    number_of_rating_recived += selectedRating;
    number_of_reviews += 5;
    let percentage = (number_of_rating_recived / number_of_reviews) * 100;
    let not_p = 100 - percentage;
    let chart = Chart.getChart(ctx);
    chart.data.datasets[0].data = [percentage, not_p];
    chart.update();
    
        number_of_rating_recived+= selectedRating
        number_of_reviews+=5
        // Append card element to review cards container
        reviewCards.appendChild(card);
    
        // Reset form inputs
        form.reset();
        cards.forEach((card,index) => {
            let star = card.querySelectorAll('.bi');
            selectedRating = 0;
            star.forEach(s =>{
                s.classList.remove('bi-star-fill');
                s.classList.add('bi-star');

                s.addEventListener('mouseover', () => {
                    for (let i = 0; i <= index; i++) {
                        star[i].classList.remove('bi-star');
                        star[i].classList.add('bi-star-fill');
                    }
                });
        
                s.addEventListener('mouseout', () => {
                    for (let i = 0; i <= index; i++) {
                        if (i >= selectedRating) {
                            star[i].classList.remove('bi-star-fill');
                            star[i].classList.add('bi-star');
                        }
                    }
                });
        
                
            })
            
        })
    
    });
});


