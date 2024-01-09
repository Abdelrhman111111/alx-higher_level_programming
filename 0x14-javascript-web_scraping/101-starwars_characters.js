#!/usr/bin/node

const req = require('request');

function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    req(url, function (err, _res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function errHandler (err) {
  console.log(err);
}

function print (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let x = 0; x < characters.length; ++x) {
        promises.push(getDataFrom(characters[x]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let x = 0; x < results.length; ++x) {
            console.log(JSON.parse(results[x]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

print(process.argv[2]);
