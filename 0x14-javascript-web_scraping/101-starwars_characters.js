#!/usr/bin/node
const requests = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
requests(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
function printCharacters (characters, index) {
  requests(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
