#!/usr/bin/node

const req =  require('request');

function get (url) {
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

function printMovieCharacters (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  get(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let i = 0; i < characters.length; ++i) {
        promises.push(get(characters[i]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

printMovieCharacters(process.argv[2]);
