#!/usr/bin/node

const d = require('./101-data').d;
const nD = {};

Object.keys(d).map(function (key) {
  if (!Array.isArray(nD[d[key]])) {
    nD[d[key]] = [];
  }
  nD[dict[key]].push(key);
});

console.log(nD);
