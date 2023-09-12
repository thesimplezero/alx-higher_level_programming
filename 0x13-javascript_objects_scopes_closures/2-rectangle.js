#!/usr/bin/node

module.exports = class Rectangle {
    constructor(w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        Object.create(null); // Create an empty object
      }
    }
  };
  