#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], function (err1, data1) {
  fs.readFile(process.argv[3], function (err2, data2) {
    if (err1 || err2) {
      return;
    }
    fs.appendFile(process.argv[4], data1, {});
    fs.appendFile(process.argv[4], data2, {});
  });
});
