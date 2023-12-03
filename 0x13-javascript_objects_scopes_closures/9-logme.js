#!/usr/bin/node

// Initialize a counter
let count = 0;

// Export the function logMe
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};

