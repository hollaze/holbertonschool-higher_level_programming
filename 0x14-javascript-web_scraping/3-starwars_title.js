#!/usr/bin/node
const request = require('request');
const episodeNumber = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episodeNumber;

request(url, function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).title);
});
