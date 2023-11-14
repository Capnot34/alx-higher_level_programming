#!/usr/bin/node
function multiply (str, num) {
  if (typeof num !== 'number') {
    console.log('Missing number of occurrences');
  } else {
    let result = '';
    for (let i = 0; i < num; i++) {
      result += str;
    }
    return result;
  }
}
