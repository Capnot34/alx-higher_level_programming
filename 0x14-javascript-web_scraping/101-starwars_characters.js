#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the Movie ID from the command line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    const movie = JSON.parse(body);

    // Iterate through characters and print one per line in the right order
    movie.characters.forEach((characterUrl, index) => {
      request.get(characterUrl, (error, response, characterBody) => {
        if (!error) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
