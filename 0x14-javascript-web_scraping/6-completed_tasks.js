#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const comp = {};
    body = JSON.parse(body);

    for (let x = 0; x < body.length; ++x) {
      const Id = body[x].userId;
      const completed = body[x].completed;

      if (completed && !comp[Id]) {
        comp[Id] = 0;
      }

      if (completed) ++comp[Id];
    }

    console.log(comp);
  }
});
