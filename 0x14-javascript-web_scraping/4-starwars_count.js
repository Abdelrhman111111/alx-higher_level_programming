#!/usr/bin/node

const request = require('request');
const starWarUri = process.argv[2];
let time = 0;

request(starWarUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const Id = character.split('/')[5];

      if (Id === '18') {
        time += 1;
      }
    }
  }

  console.log(time);
});
