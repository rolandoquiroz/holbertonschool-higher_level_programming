#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], function (err, content) {
  if (err) {
    return;
  }
  fs.writeFile(process.argv[4], content, { flag: 'a+' }, (err) => {
    if (err) {
        return;
    }
  });
});
fs.readFile(process.argv[3], function (err, content) {
  if (err) {
    return;
  }
  fs.writeFile(process.argv[4], '\n' + content, { flag: 'a+' }, (err) => {
    if (err) {
        return;
    }
  });
});
