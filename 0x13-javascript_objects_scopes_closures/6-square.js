#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(char || 'X');
      }
      console.log();
    }
  }
}
module.exports = Square;
