#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // http://loripsum.net/api
const fileName = process.argv[3];
const fs = require('fs');

request(url, 'utf-8', function (error, response, body) {
  if (error) throw error;
  fs.writeFile(fileName, body, 'utf-8', (err, data) => {
    if (err) throw err;
  });
});
