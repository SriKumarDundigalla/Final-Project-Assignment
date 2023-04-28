function toggleDarkMode() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.toggle("dark-mode");
}
// const starIcons = document.querySelectorAll('.rating');

// starIcons.forEach((starIcon, index) => {
//   starIcon.addEventListener('mouseover', () => {
//     for (let i = 0; i <= index; i++) {
//       starIcons[i].classList.remove('bi-star');
//       starIcons[i].classList.add('bi-star-fill');
//     }
//   });

//   starIcon.addEventListener('mouseout', () => {
//     for (let i = 0; i <= index; i++) {
//       starIcons[i].classList.remove('bi-star-fill');
//       starIcons[i].classList.add('bi-star');
//     }
//   });
// });
