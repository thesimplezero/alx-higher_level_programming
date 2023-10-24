#!/usr/bin/node

// Import the module
const fs = require('fs');

// The argument is the file path
const file = process.argv[2];

// Read the file
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});