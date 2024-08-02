#!/usr/bin/node
const request = require('request');
const f = require('fs');
request(process.argv[2]).pipe(f.createWriteStream(process.argv[3]));
