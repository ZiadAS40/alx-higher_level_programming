#!/usr/bin/node
const f = require('f');
const a = f.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const b = f.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });
const c = a.concat(b);
f.writeFile(process.argv[4], c, 'utf8', function (err, result) { if (err) console.log('error', err); });
