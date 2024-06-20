#!/usr/bin/node
const list = require('./100-data').list;
const myArr = list.map((a, b) => a * b);
console.log(list);
console.log(myArr);
