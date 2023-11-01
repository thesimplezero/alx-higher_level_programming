// Using jQuery's AJAX for GET request
$.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Extract the translation of "hello" from the fetched data
      const translation = data.hello;
  
      // Display the translation in the <div> with ID "hello"
      $('DIV#hello').text(translation);
    }
  });
  