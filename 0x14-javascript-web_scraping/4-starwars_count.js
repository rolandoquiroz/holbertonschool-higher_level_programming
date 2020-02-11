#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let appearances = 0;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('/18/')) {
          appearances += 1;
        }
      }
    }
    console.log(appearances);
  }
});
