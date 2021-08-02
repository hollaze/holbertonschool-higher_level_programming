#!/usr/bin/node
const argv = process.argv;
const res = 0;

function add (a, b) {
  if (a === undefined || isNaN(parseInt(a)) ||
        b === undefined || isNaN(parseInt(b))) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}

add(argv[2], argv[3]);
