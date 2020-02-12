#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const alltasks = JSON.parse(body);
    const tasksdone = {};
    let i = 0;
    while (i < alltasks.length) {
      if (alltasks[i].completed === true) {
        if (tasksdone[alltasks[i].userId]) {
          tasksdone[alltasks[i].userId] += 1;
        } else {
          tasksdone[alltasks[i].userId] = 1;
        }
      }
      i++;
    }
    console.log(tasksdone);
  }
});
