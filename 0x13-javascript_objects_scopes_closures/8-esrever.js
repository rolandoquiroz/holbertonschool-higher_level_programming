#!/usr/bin/node
exports.esrever = function (list) {
  const reverted = [];
  for (let i = (list.length) - 1; i > -1; i--) {
    reverted.push(list[i]);
  }
  return reverted;
};
