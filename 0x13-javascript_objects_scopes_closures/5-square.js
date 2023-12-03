#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// Create the Square class that inherits from Rectangle
class Square extends Rectangle {
  // Constructor that takes one argument: size
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) with size as both width and height
    super(size, size);
  }
}

// Export the Square class
module.exports = Square;
