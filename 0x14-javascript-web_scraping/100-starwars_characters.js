#!/usr/bin/node
const requests = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
requests(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterUrl) => {
      requests(characterUrl, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
