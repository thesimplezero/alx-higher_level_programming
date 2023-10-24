#!/usr/bin/node

const request = require('request');

// The first argument is the URL to request (GET)
const url = process.argv[2];

if (!url) {
  console.error('Usage: node script.js <URL>');
  process.exit(1);
}

// Make an HTTP GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Status Code:', response.statusCode);
  }
});
