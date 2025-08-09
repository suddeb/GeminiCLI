const headerText = document.getElementById('header-text');

const colors = ['#e74c3c', '#8e44ad', '#3498db', '#e67e22', '#2ecc71', '#1abc9c'];
let currentColorIndex = 0;

headerText.addEventListener('click', () => {
    currentColorIndex = (currentColorIndex + 1) % colors.length;
    headerText.style.color = colors[currentColorIndex];
});