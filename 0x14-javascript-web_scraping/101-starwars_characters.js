#!/usr/bin/node
const rqst = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
rqst(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    printChar(chars, 0);
  }
});

function printChar (chars, index) {
  rqst(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printChar(chars, index + 1);
      }
    }
  });
}