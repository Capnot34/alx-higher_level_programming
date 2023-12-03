#!/usr/bin/node

// Export the function converter
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
