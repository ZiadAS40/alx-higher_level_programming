#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let counter = 0;
    const constUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

    results.forEach(result => {
      result.characters.forEach((char) => {
        if (constUrl === char) {
          counter++;
        }
      });
    });
    console.log(counter);
  }
});
