#!/usr/bin/node
const n = process.argv[2];

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return (factorial(n - 1) * n);
  }
}

if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(Number(n)));
}
