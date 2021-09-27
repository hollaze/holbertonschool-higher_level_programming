#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // https://jsonplaceholder.typicode.com/todos

request(url, function (error, response, body) {
  if (error)  return (console.log(error));
  const parsedBody = JSON.parse(body);

  const completedTasks = {};

  for (let i = 1; i < parsedBody.length; i++) {
    if (parsedBody[i].completed) {
        const userId = parsedBody[i].userId;
      if (userId !== undefined) {
        completedTasks[userId] += 1;
      } else {
        completedTasks[userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
