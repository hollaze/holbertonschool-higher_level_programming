#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (let i = 0; list[i]; i++) {
    if (searchElement === list[i]) {
      occurences += 1;
    }
  }
  return occurences;
};
