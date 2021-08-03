#!/usr/bin/node
let nbArguments = 0;
exports.logMe = function (item) {
  console.log(nbArguments + ':' + ' ' + item);
  nbArguments += 1;
};
