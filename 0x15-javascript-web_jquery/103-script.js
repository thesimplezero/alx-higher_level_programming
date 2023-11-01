// When the document is ready, set up event handlers
$(document).ready(function () {
    // Event handler for button click
    $('#btn_translate').click(function () {
      translateHello();
    });
  
    // Event handler for Enter key press in the input field
    $('#language_code').keypress(function (event) {
      if (event.which === 13) {
        translateHello();
      }
    });
  
    // Function to send a GET request and update the displayed message
    function translateHello() {
      const languageCode = $('#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
  