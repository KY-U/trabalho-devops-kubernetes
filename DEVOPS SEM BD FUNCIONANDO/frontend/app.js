document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('movie-form');
    const movieList = document.getElementById('movie-list');
    
    // Fetch movies on page load
    function fetchMovies() {
        fetch('/api/movies')
            .then(response => response.json())
            .then(movies => {
                movieList.innerHTML = '';
                movies.forEach(movie => {
                    const li = document.createElement('li');
                    li.textContent = `${movie.title} (${movie.year})`;
                    
                    // Add a remove button for each movie
                    const removeButton = document.createElement('button');
                    removeButton.textContent = 'Remove';
                    removeButton.addEventListener('click', () => {
                        removeMovie(movie.title);
                    });
                    
                    li.appendChild(removeButton);
                    movieList.appendChild(li);
                });
            })
            .catch(error => {
                console.error('Error fetching movies:', error);
                movieList.innerHTML = 'Error loading movies';
            });
    }
    
    function removeMovie(title) {
        fetch(`/api/movies/${title}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(() => {
            fetchMovies(); // Refresh the movie list
        })
        .catch(error => {
            console.error('Error removing movie:', error);
        });
    }
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const title = document.getElementById('title').value;
        const year = document.getElementById('year').value;
        
        fetch('/api/movies', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, year })
        })
        .then(response => response.json())
        .then(() => {
            // Clear form and fetch movies again
            form.reset();
            fetchMovies();
        })
        .catch(error => {
            console.error('Error adding movie:', error);
        });
    });
    
    fetchMovies(); // Initial fetch on page load
});