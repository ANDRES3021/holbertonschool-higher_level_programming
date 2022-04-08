#!/usr/bin/node
exports.esrever = function (list) {
  const secondList = [];
  let iterator = 0;
  while (list[iterator]) {
    secondList.push(list[list.length - (iterator + 1)]);
    iterator++;
  }
  return (secondList);
};
