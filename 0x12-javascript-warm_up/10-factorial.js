#!/usr/bin/node

// Import the built-in "process" module
const process = require('process');

// Get the first command-line argument and convert it to an integer
const firstArg = process.argv[2];
const num = parseInt(firstArg);

// Define a recursive function to calculate the factorial
function calculateFactorial(x) {
  if (isNaN(x) || x < 0) {
    // If x is NaN or negative, return 1
    return 1;
  } else if (x === 0) {
    // If x is 0, factorial is 1
    return 1;
  } else {
    // Otherwise, calculate factorial recursively
    return x * calculateFactorial(x - 1);
  }
}

// Calculate and print the factorial
console.log(calculateFactorial(num));
