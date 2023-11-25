#!/usr/bin/node

// Recursive function to compute factorial
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  } else if (n === 0 || n === 1) {
    return 1; // Factorial of 0 or 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive call to compute factorial
  }
}

// Get the argument from the command line
const num = parseInt(process.argv[2]);

// Compute and print the factorial
console.log(factorial(num));
