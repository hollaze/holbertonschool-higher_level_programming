#!/usr/bin/node
const argv = process.argv;
const numArr = []; let j = 2;

function bubbleSort (arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < (arr.length - i - 1); j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

if (argv[2] === undefined || argv.length === 1) {
  console.log(0);
} else {
  for (let i = 2; argv[i]; i++) {
    numArr[i] = parseInt(argv[i]);
  }

  bubbleSort(numArr);

  while (j < numArr.length - 2) {
    j++;
  }

  console.log(numArr[j]);
}
