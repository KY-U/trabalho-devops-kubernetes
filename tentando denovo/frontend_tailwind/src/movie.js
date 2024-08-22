document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const movieId = urlParams.get('id');
  
    fetch(`/api/movies/${movieId}`)
      .then(response => response.json())
      .then(movie => {
        const movieDetails = document.getElementById('movie-details');
        movieDetails.innerHTML = `
          <h2 class="text-2xl font-bold">${movie.title}</h2>
          <p>${movie.description}</p>
          <p><strong>Gênero:</strong> ${movie.genre}</p>
          <p><strong>Ano:</strong> ${movie.year}</p>
        `;
      })
      .catch(error => console.error('Error fetching movie details:', error));
  });