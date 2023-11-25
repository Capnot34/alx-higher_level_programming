#!/usr/bin/node

// Check if an argument is passed
if (process.argv[2]) {
  // If argument is passed, print it
  console.log(process.argv[2]);
} else {
  // If no argument is passed, print "No argument"
  console.log('No argument');
}
