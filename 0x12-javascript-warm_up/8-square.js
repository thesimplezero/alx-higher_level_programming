#!/usr/bin/node

// Import the built-in "process" module
const process = require('process');

// Get the first command-line argument provided to the script
const firstArg = process.argv[2];

// Attempt to convert the first argument to an integer
const size = parseInt(firstArg);

// Check if the conversion was successful (i.e., if it's a valid integer)
if (!isNaN(size)) {
  if (size > 0) {
    // Loop to generate rows
    for (let i = 0; i < size; i++) {
      let row = '';
      // Loop to generate columns
      for (let j = 0; j < size; j++) {
        row += 'X'; // Append 'X' for each column
      }
      console.log(row); // Print the row
    }
  }
} else {
  // If it's not a valid integer, print "Missing size"
  console.log('Missing size');
}
