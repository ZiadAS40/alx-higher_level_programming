#!/usr/bin/node
const arr = process.argv;
arr.splice(0, 2);
function secondBig (array) {
  if (array.length <= 1) {
    return (0);
  }
  array.sort((a, b) => Number(a) - Number(b));
  return (Number(array[array.length - 2]));
}
console.log(secondBig(arr));
