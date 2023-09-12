#!/usr/bin/node

exports.logMe = function () {
    let count = 0; // Initialize count in the function scope
  
    return function (item) {
      console.log(`${count++}: ${item}`);
    };
  }();
  