#!/usr/bin/node
const request = require('request');
const character = 'https://swapi-api.hbtn.io/api/people/18/'; // Wedge Antilles

request(process.argv[2].replace(process.argv[2], character), function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).films.length);
});
