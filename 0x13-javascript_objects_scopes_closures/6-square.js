#!/usr/bin/node
const Rectangule = require('./4-rectangle');
class Square extends Rectangule {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == undefined) {
      c = 'X';
    }
    let count = 0;
    while (count < this.width) {
      console.log(c.repeat(this.width));
      count++;
    }
  }
}

module.exports = Square;
