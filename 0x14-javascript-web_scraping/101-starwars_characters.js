#!/usr/bin/node
const movieNumber = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieNumber;
const request = require('request');

request(url, async (error, response, body) => {
  if (error) throw error;
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    const name = await new Promise((resolve, reject) => {
      request(characters[i], function (error, response, body) {
        if (error) return reject(error);
        resolve(JSON.parse(body).name);
      });
    });
    console.log(name);
  }
});
