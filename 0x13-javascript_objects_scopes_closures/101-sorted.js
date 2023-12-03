#!/usr/bin/node

// Import the dictionary from 101-data.js
const { dict } = require('./101-data');

// Create a new dictionary with user ids grouped by occurrences
const newDict = {};
for (const key in dict) {
  const occurrences = dict[key];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(key);
}

// Print the new dictionary
console.log(newDict);
