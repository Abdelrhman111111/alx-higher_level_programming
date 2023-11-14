#!/usr/bin/node

// .............................

const Rect = require('./4-rectangle');

module.exports = class Square extends Rect {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }
};
