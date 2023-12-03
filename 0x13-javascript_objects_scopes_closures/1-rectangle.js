#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

// Example usage
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);
