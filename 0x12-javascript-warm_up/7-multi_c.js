#!/usr/bin/node

let printt = parseInt(process.argv[2]);
if (isNaN(printt) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (printt > 0) {
    console.log('C is fun');
    printt--;
  }
}
