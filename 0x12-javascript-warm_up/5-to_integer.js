#!/usr/bin/node

// Get the first argument from the command line
const firstArg = process.argv[2];

// Convert the argument to an integer using parseInt
const convertedNumber = parseInt(firstArg);

// Check if the conversion resulted in a valid integer
if (!isNaN(convertedNumber)) {
  // If it's a valid integer, print the message
  console.log('My number: ' + convertedNumber);
} else {
  // If it's not a valid integer, print "Not a number"
  console.log('Not a number');
}
