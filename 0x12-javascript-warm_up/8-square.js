#!/usr/bin/node

// Get the size of the square from the command line
const size = parseInt(process.argv[2]);

// Check if the size is a valid integer
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  // Loop through each row and column to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  // If size is less than or equal to 0, don't print anything
}
