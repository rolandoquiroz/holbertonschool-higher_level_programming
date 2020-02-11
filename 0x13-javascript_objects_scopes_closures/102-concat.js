#!/usr/bin/node
const fs = require('fs');
if (process.argv[2] && process.argv[3] && process.argv[4]) {
  const contents1 = fs.readFileSync(process.argv[2], 'utf8');
  const contents2 = fs.readFileSync(process.argv[3], 'utf8');
  const content = contents1 + '\n' + contents2;
  fs.appendFile(process.argv[4], content, function (err) { if (err) throw err; });
}
