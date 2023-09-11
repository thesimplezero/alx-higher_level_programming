#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length <= 2) {
  // No argument passed or only one argument
  console.log('0');
} else {
  const array = args.slice(2).map(Number); // Convert and slice the arguments
  array.sort((a, b) => a - b); // Sort the array in ascending order
  console.log(array[array.length - 2]); // Print the second largest element
}
