#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  const res = parseInt(a) + parseInt(b);
  if (a === undefined || isNaN(parseInt(a)) ||
        b === undefined || isNaN(parseInt(b))) {
    console.log('NaN');
  } else {
    console.log(res);
  }
}

add(argv[2], argv[3]);
