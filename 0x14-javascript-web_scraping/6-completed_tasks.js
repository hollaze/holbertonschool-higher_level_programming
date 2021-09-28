#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // https://jsonplaceholder.typicode.com/todos
const completedTasks = {};

request(url, function (error, response, body) {
  if (error) return (console.log(error));
  const parsedBody = JSON.parse(body);

  parsedBody.forEach(element => {
    if (element.completed) {
      if (element.userId in completedTasks) {
        completedTasks[element.userId] += 1;
      } else {
        completedTasks[element.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
