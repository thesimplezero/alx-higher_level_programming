#!/usr/bin/node

const process = require('process');

const firstArg = process.argv[2];
const secondArg = process.argv[3];

console.log(firstArg + ' is ' + secondArg);
