#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let step = 0;
    while (step < this.height) {
      console.log('X'.repeat(this.width));
      step += 1;
    }
  }
}

module.exports = Rectangle;
