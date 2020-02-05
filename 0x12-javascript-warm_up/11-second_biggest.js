#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const ins = process.argv.slice(2);
  const nums = ins.map(Number);
  const sorted = nums.sort(function (a, b) { return b - a; });
  console.log(sorted[1]);
}
