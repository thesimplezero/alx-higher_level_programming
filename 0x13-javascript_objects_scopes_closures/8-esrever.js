#!/usr/bin/node

exports.esrever = function (list) {
    const length = list.length;
    const middle = Math.floor(length / 2);
  
    for (let i = 0; i < middle; i++) {
      const temp = list[i];
      list[i] = list[length - i - 1];
      list[length - i - 1] = temp;
    }
    
    return list;
  };
  