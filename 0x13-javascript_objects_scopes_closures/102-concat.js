#!/usr/bin/node
const fs = require('fs');
if (process.argv[2] && process.argv[3] && process.argv[4]) {
  const content1 = fs.readFileSync(process.argv[2], 'utf8');
  fs.appendFile(process.argv[4], content1, function (err) { if (err) throw err; });
  const content2 = fs.readFileSync(process.argv[3], 'utf8');
  fs.appendFile(process.argv[4], content2, function (err) { if (err) throw err; });
}
