#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
    this.size = size;
  }

  charPrint(c) {
    if (c === undefined) {
      this.print();
    }
    else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
