#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // https://jsonplaceholder.typicode.com/todos
const completedTasks = {};

request(url, function (error, response, body) {
  if (error)  console.log(error);
  const parsedBody = JSON.parse(body);

  for (let i = 1; i < parsedBody.length; i++) {
    if (parsedBody[i].completed === true) {
      if (parsedBody[i].userId in completedTasks) {
        completedTasks[parsedBody[i].userId] += 1;
      } else {
        completedTasks[parsedBody[i].userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
