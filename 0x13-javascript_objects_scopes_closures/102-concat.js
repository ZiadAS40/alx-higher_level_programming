#!/usr/bin/node
const fs = require('fs');
const a = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const b = fs.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });
const c = a.concat(b);
fs.writeFile(process.argv[4], c, 'utf8', function (err, result) { if (err) console.log('error', err); });
