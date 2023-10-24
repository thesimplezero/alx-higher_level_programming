#!/usr/bin/node

const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Create an empty dictionary to store user counts
const userCounts = {};

// Make an HTTP GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);

    // Iterate through the data and count completed tasks per user
    data.forEach((result) => {
      if (result.completed === true) {
        const userId = result.userId;
        userCounts[userId] = (userCounts[userId] || 0) + 1;
      }
    });

    console.log(userCounts);
  }
});
