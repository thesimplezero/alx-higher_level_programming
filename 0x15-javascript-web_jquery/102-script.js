// Wait for the document to be fully loaded
$(document).ready(function () {
    // Event handler for button click
    $('#btn_translate').click(function () {
      // Get the language code from the input field
      const languageCode = $('#language_code').val();
      
      // Send a GET request to fetch the translated "Hello" message
      $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function (data) {
        // Update the content of the HTML element with ID 'hello'
        $('#hello').text(data.hello);
      });
    });
  });
  