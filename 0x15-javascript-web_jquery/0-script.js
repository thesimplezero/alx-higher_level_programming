// Select the element
const element = document.querySelector('header');

// Check if element was found
if (element) {
    // Set colour
    element.style.color = '#FF0000';
} else {
    console.error('Header element not found');
}