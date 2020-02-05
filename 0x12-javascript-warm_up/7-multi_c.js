#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2]) > 0) {
  const x = parseInt(process.argv[2]);
  let i;
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
