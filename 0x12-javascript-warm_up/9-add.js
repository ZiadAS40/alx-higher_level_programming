#!/usr/bin/node
const arr = process.argv;
const x = arr[2];
const y = arr[3];
function add (a, b) {
  a = arr[2];
  b = arr[3];
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(Number(a) + Number(b));
  }
}
add(x, y);
