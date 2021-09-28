#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (error) return (console.log(error));
  const results = JSON.parse(body).results;
  results.forEach(episodeId => {
    episodeId.characters.forEach(character => {
      if (character.indexOf('people/18') >= 0) {
        count += 1;
      }
    });
  });
  console.log(count);
});
