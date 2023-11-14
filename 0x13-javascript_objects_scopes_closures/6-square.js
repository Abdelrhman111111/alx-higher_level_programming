#!/usr/bin/node

// ......................................

const OldS = require('./5-square');

module.exports = class Square extends OldS {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
