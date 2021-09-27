#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // https://jsonplaceholder.typicode.com/todos

request(url, function (error, response, body) {
  if (error)  console.log(error);
  const parsedBody = JSON.parse(body);

  const completedTasks = {};

  for (let i = 1; i < parsedBody.length; i++) {
    if (parsedBody[i].completed) {
      if (parsedBody[i].userId !== undefined) {
        completedTasks[parsedBody[i].userId] += 1;
      } else {
        completedTasks[parsedBody[i].userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
