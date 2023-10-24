#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from command-line arguments
const apiUrl = process.argv[2];
const file = process.argv[3];

// Make an HTTP GET request to the specified URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Write the response to the specified file
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) {
        console.error('Write error:', err);
      } else {
        console.log('Response saved to', file);
      }
    });
  }
});
