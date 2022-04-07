#!/usr/bin/node
const Rectangule = require('./4-rectangle');
class Square extends Rectangule {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
