document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/movies')
      .then(response => response.json())
      .then(movies => {
        const movieList = document.getElementById('movie-list');
        movieList.innerHTML = movies.map(movie => `
          <div class="bg-white p-4 rounded-lg shadow-md">
            <h2 class="text-xl font-bold">${movie.title}</h2>
            <p>${movie.description}</p>
            <a href="/movie-details.html?id=${movie.id}" class="text-blue-500">Ver detalhes</a>
          </div>
        `).join('');
      })
      .catch(error => console.error('Error fetching movies:', error));
  });