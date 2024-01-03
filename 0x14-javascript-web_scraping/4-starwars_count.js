#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the command line arguments
const characterId = 18; // Wedge Antilles character ID

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    const films = JSON.parse(body).results;
    const wedgeMovies = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(wedgeMovies.length); // Print the number of movies
  }
});
