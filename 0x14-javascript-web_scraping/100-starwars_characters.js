#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const allcharacters = JSON.parse(body)['characters'];
    let i = 0;
    while (i < allcharacters.length) {
      request(allcharacters[i], function (err, response, body) {
        if (!err && response.statusCode === 200) {
          console.log(JSON.parse(body)['name']);
        }
      });
      i++;
    }
  }
});