#!/usr/bin/node
const url = 'http://swapi.co/api/films/';
require('request').get(url + process.argv[2] + '/', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
