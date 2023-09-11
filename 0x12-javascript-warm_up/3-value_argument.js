#!/usr/bin/node

// import built-in module "process"
const process = require('process');

// Check if there is a first argument
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
