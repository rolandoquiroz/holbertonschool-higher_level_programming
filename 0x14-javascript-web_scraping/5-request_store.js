#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (!err && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, function (err) {
      if (err) throw err;
    });
  }
});
