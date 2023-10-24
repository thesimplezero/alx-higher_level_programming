#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;

    const moviesWithWedge = results.reduce((count, movie) => {
      const hasWedge = movie.characters.some(character => character.endsWith('/18/'));
      return count + (hasWedge ? 1 : 0);
    }, 0);

    console.log(`Number of movies with Wedge Antilles: ${moviesWithWedge}`);
  } else {
    console.error('Error:', error);
  }
});
