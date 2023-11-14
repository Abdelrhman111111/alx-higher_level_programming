#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const s = process.argv.length;
  const is = [];
  for (let i = 2; i < s; i++) {
    is[i - 2] = parseInt(process.argv[i]);
  }
  is.sort(function (a, b) { return b - a; });
  console.log(is[1]);
}
