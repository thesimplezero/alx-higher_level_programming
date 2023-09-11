#!/usr/bin/node

// Import the built-in "process" module
const process = require('process');

// Get the first and second command-line arguments and convert them to integers
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// Define the add function
function add(a, b) {
  return a + b;
}

// Call the add function with the two integers and print the result
console.log(add(firstArg, secondArg));
