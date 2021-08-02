#!/usr/bin/node
const argv = process.argv;

function factorial(n) {
    let res = 1;
    if (n > 0) {
        res = factorial(n - 1) * n;
    }
    return res;
}

console.log(factorial(parseInt(argv[2])));