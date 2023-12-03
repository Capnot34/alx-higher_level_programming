#!/usr/bin/node

// Import the required modules
const fs = require('fs');

// Read the contents of the first source file
const fileAContent = fs.readFileSync(process.argv[2], 'utf8');

// Read the contents of the second source file
const fileBContent = fs.readFileSync(process.argv[3], 'utf8');

// Concatenate the contents and write to the destination file
fs.writeFileSync(process.argv[4], fileAContent + fileBContent);
