// Wait for the document to be fully loaded
$(document).ready(function () {
    // Event handler for adding an item to the list
    $('#add_item').click(function () {
      // Create a new list item and append it to the <ul> with class 'my_list'
      $('<li>Item</li>').appendTo('ul.my_list');
    });
  
    // Event handler for removing the last item from the list
    $('#remove_item').click(function () {
      // Remove the last <li> element from the <ul> with class 'my_list'
      $('ul.my_list li:last').remove();
    });
  
    // Event handler for clearing the entire list
    $('#clear_list').click(function () {
      // Empty the entire <ul> with class 'my_list'
      $('ul.my_list').empty();
    });
  });
  