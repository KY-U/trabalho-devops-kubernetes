document.addEventListener('DOMContentLoaded', () => {
    const moviesList = document.getElementById('moviesList');
    const addMovieForm = document.getElementById('addMovieForm');

    function fetchMovies() {
        fetch('/api/movies')
            .then(response => response.json())
            .then(data => {
                moviesList.innerHTML = '';
                data.forEach(movie => {
                    const li = document.createElement('li');
                    li.textContent = `${movie.title} (${movie.year})`;
                    li.innerHTML += ` <button onclick="deleteMovie(${movie.id})" class="text-red-500">Delete</button>`;
                    moviesList.appendChild(li);
                });
            });
    }

    addMovieForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const year = document.getElementById('year').value;

        fetch('/api/movies', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, year })
        }).then(() => {
            fetchMovies();
            addMovieForm.reset();
        });
    });

    fetchMovies();
});

function deleteMovie(id) {
    fetch(`/api/movies/${id}`, {
        method: 'DELETE'
    }).then(() => {
        fetchMovies();
    });
}