#!/usr/bin/node
exports.esrever = function (list) {
    const revList = [];
  for (let i = 0, j = list.length - 1; list[i] && j >= 0; i++, j--) {
      revList[i] = list[j];
  }
  return (revList);
};
