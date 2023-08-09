#!/usr/bin/env node
const request = require('request');

const id = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getRequest(uri, attr) {
  const getPromise = new Promise((resolve, reject) => {
    request({ uri: uri, json: true }, (error, res, body) => {
      if (error) {
        reject(error);
      } else if (res.statusCode !== 200) {
        reject(error);
      } else {
        resolve(body[`${attr}`]);
      }
    });
  });

  return getPromise;
}

async function getFilmById(uri, attr) {
  return await getRequest(uri, attr);
}

async function getCharacters() {
  charactersUriList = await getFilmById(filmUrl, 'characters');
  for (const link of await charactersUriList) {
    console.log(await getRequest(link, 'name'));
  }
}

getCharacters();
