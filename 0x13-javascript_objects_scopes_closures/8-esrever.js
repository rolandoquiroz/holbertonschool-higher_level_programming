#!/usr/bin/node
exports.esrever = function (list) {
  const reverted = [];
  for (var i = (list.length - 1), j = 0; i > -1, j < list.length; i--, j++) {
    reverted[i] = list[j];
  }
  return reverted;
};
