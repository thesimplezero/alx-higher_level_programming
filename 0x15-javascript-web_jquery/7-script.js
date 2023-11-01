//  Using jQuery AJAX to make a GET request to the Star Wars API

$.ajax({
    // Define the URL of the API endpoint
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  
    // Specify the HTTP method as 'GET' to retrieve data
    method: 'GET',
  
    // Set the expected data type as JSON
    datatype: 'json',
  
    // Define a callback function to handle a successful response
    success: function (data) {
      // Extract the character's name from the fetched data
      const characterName = data.name;
  
      // Display the character's name in the specified HTML div element
      $('DIV#character').text(characterName);
    }
  });
  