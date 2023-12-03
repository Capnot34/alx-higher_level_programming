#!/usr/bin/node

// Import the list from 100-data.js
const { list } = require('./100-data');

// Map the list to a new list based on the index
const newList = list.map((value, index) => value * index);

// Print both the initial and new lists
console.log(list);
console.log(newList);

