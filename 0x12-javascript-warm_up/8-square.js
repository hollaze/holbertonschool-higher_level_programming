#!/usr/bin/node
const argv = process.argv;
const stringX = 'X'; let str = '';

if (argv[2] === undefined || isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    str += stringX;
    for (let j = 0; j < parseInt(argv[2]); j++) {
      if (i === parseInt(argv[2]) - 1) {
        console.log(str);
      }
    }
  }
}
