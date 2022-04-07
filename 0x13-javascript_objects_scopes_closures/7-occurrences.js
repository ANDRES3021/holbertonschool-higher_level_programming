#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let position = 0;
  while (list[position]) {
    if (searchElement === list[position]) {
      counter++;
    }
    position++;
  }
  return (counter);
};
