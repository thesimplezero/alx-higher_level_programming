#!/usr/bin/node

// Import the built-in "process" module
const process = require('process');

// Get the first command-line argument and convert it to an integer
const firstArg = process.argv[2];
const num = parseInt(firstArg);

// Define a recursive function to calculate the factorial
function calculateFactorial(x) {
  if (isNaN(x) || x === 0) {
    // If x is NaN or 0, return 1
    return 1;
  } else {
    // Otherwise, calculate factorial recursively
    return x * calculateFactorial(x - 1);
  }
}

// Check if the input is a valid number
if (!isNaN(num)) {
  // If it's a number, calculate and print the factorial
  console.log(calculateFactorial(num));
} else {
  // If it's not a valid number, print 1
  console.log('1');
}
