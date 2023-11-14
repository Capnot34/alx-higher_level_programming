#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if both width and height are greater than 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// Export the Rectangle class
module.exports = Rectangle;
