#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Construct the API URL using the movie ID
const apiurl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the API
request(apiurl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response and print the movie title
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
