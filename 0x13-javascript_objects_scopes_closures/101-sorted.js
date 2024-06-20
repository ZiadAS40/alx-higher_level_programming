#!/usr/bin/node
const { dict } = require('./101-data');
const val = Object.entries(dict).reduce((al, [key, value]) => {
  al[value] = al[value] ? [...al[value], key] : [key];
  return al;
}, {});
console.log(val);
