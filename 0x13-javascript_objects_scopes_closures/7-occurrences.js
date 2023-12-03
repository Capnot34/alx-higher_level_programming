#!/usr/bin/node

// Export the function nbOccurences
exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
