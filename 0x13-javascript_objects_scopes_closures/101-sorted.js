#!/usr/bin/node

const d = require('./101-data').d;
const newD = {};

Object.keys(d).map(function (key) {
  if (!Array.isArray(newD[d[key]])) {
    newD[d[key]] = [];
  }
  newD[d[key]].push(key);
});

console.log(newD);
