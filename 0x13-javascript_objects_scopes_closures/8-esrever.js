#!/usr/bin/node

// Export the function esrever
exports.esrever = function (list) {
  return list.reduceRight((reversed, element) => {
    reversed.push(element);
    return reversed;
  }, []);
};
