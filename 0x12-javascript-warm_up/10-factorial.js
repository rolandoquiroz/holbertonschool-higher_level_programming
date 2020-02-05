#!/usr/bin/node

function facto (n) {
  if ((isNaN(n) || (parseInt(n)) === 0)) {
    return 1;
  }
  return (parseInt(n) * facto(parseInt(n) - 1));
}

console.log(facto(process.argv[2]));
