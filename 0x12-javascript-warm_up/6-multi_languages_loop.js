#!/usr/bin/node

const myVars = {
  i: 'C is fun',
  b: 'Python is cool',
  c: 'JavaScript is amazing'
};

for (const items in myVars) {
  console.log(myVars[items]);
}
