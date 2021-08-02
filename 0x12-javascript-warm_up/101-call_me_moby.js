#!/usr/bin/node

exports.callMeMoby = function (x, functionName) {
  for (let i = 0; i < x; i++) {
    functionName();
  }
};
