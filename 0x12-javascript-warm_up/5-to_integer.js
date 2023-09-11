#!/usr/bin/node

// Import the built-in "process" module
const process = require('process');

// Get the first command-line argument provided to the script
const firstArg = process.argv[2];

// Attempt to convert the first argument to an integer
const convertedFirstArg = parseInt(firstArg);

// Check if the conversion was successful (i.e., if it's a valid integer)
if (!isNaN(convertedFirstArg)) {
  // If it's a valid integer, print it
  console.log('My number:', convertedFirstArg);
} else {
  // If it's not a valid integer, print "Not a number"
  console.log('Not a number');
}
