#!/usr/bin/node

// Get the list of arguments from the command line
const args = process.argv.slice(2);

// Check the number of arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert the arguments to integers and sort them in descending order
  const sortedArgs = args.map(Number).sort((a, b) => b - a);

  // Print the second biggest integer
  console.log(sortedArgs[1]);
}
