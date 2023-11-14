#!/usr/bin/node

// ..............................

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let x = 0; x < this.height; ++x) {
      let y = 0;

      for (; y < this.width; ++y) {
        process.stdout.write('X');
      }

      if (y === this.width) {
        console.log('');
      }
    }
  }
};
