#!/usr/bin/node
const request = require('request');
const resultObj = {};

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    for (let i = 1; i <= 10; i++) {
      const userTodos = todos.filter(todo => todo.userId === i && todo.completed === true);

      resultObj[i] = userTodos.length;
    }
    console.log(resultObj);
  }
});
