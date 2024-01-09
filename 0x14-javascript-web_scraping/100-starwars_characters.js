#!/usr/bin/node

const req = require('request');
const Uri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

req(Uri, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let x = 0; x < characters.length; ++x) {
    req(characters[x], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
