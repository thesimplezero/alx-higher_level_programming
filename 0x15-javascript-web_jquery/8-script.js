// Using jQuery's AJAX for GET request
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function (data) {
      // Extract movie titles from the fetched data and map them to an array
      const movieTitles = data.results.map(function (movie) {
        return movie.title;
      });
  
      // Select the HTML <ul> element with the ID 'list_movies'
      const listElement = $('UL#list_movies');
      
      // Loop through the movie titles and append them as list items to the <ul>
      $.each(movieTitles, function (index, title) {
        const listItem = $('<li>' + title + '</li>');
        listElement.append(listItem);
      });
    }
  });
  