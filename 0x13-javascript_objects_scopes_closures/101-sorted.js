#!/usr/bin/node
const dictio = require('./101-data').dict;
const mydict = {};
for (const key in dictio) {
  if (mydict[dictio[key]] === undefined) {
    mydict[dictio[key]] = [];
  }
  mydict[dictio[key]].push(key);
}
console.log(mydict);
