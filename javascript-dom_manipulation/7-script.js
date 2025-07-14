#!/usr/bin/node

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.querySelector('#list_movies');
    for (const film of data.results) {
      const li = document.createElement('li');
      li.textContent = film.title;
      listMovies.appendChild(li);
    }

    console.log(data.results);
  });
