// jquery script
$(document).ready(function () {
    // Use jquery selector
    const element = $('header');
  
    // Check if header was found
    if (element) {
      // Use css to set colour
      element.css('color', '#FF0000');
    } else {
      console.error('Header element not found');
    }
  });