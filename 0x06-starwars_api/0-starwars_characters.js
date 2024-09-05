#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a GET request to the Star Wars API for the movie information
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body to JSON format
  const movieData = JSON.parse(body);

  // Extract the characters' URLs from the movie data
  const characterUrls = movieData.characters;

  // Fetch and display each character's name in the correct order
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
