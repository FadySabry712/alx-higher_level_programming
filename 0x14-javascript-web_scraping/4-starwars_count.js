#!/usr/bin/node
const request = require('requests');
const apiUrl = process.argv[2];
request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
    return;
  }

  let count = 0;

  body.results.forEach(film => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });

  console.log(count);
});
