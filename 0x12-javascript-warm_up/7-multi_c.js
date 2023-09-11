#!/usr/bin/node

// Import the built-in "process" module
const process = require('process');

// Get the first command-line argument provided to the script
const firstArg = process.argv[2];

// Attempt to convert the first argument to an integer
const x = parseInt(firstArg);

// Check if the conversion was successful (i.e., if it's a valid integer)
if (!isNaN(x)) {
  // Loop and print "C is fun" x times
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  // If it's not a valid integer, print "Missing number of occurrences"
  console.log('Missing number of occurrences');
}
