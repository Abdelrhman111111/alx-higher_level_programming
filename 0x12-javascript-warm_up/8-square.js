#!/usr/bin/node

let s = parseInt(process.argv[2]);
if (isNaN(s) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let p = 'X';
for (let i = 0; i < s - 1; i++) {
  p += 'X';
}
while (s > 0) {
  console.log(p);
  s--;
}
