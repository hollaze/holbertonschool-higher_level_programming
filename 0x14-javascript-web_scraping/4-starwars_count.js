#!/usr/bin/node
const request = require('request');
const character = 'https://swapi-api.hbtn.io/api/people/18/'; // Wedge Antilles
const url = process.argv[2];
const episodeId = [];
let count = 0;

request(url, function (error, response, body) {
  if (error) return (console.log(error));
  const results = JSON.parse(body).results;
  for (let i = 0; i < results.length; i++) {
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j] === character &&
        !(results[i].episode_id in episodeId)) {
        count += 1;
      }
    }
  }

  console.log(count);
});
