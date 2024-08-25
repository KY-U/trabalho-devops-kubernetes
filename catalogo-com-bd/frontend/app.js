//const apiUrl = 'http://python_backend:5000'; // URL do backend

//Com o proxy reverso:
const apiUrl = '/api';
//Busca os filmes
async function fetchMovies() {
    try {
        const response = await fetch(`${apiUrl}/movies`);
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'An error occurred while fetching movies');
        }
        const movies = await response.json();
        const tableBody = document.querySelector('#movies-table tbody');
        tableBody.innerHTML = '';

        movies.forEach(movie => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${movie.id}</td>
                <td>${movie.title}</td>
                <td>${movie.release_year}</td>
                <td>${movie.description}</td>
                <td><button onclick="deleteMovie(${movie.id})">Delete</button></td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        alert(`Error: ${error.message}`);
        console.error('Error fetching movies:', error);
    }
}

//Adiciona filme novo
document.querySelector('#add-movie-form').addEventListener('submit', async event => {
    event.preventDefault();

    const title = document.querySelector('#title').value;
    const release_year = document.querySelector('#release_year').value;
    const description = document.querySelector('#description').value;

    try {
        const response = await fetch(`${apiUrl}/movies`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title,
                release_year,
                description
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Movie added:', result);

        //alert('Movie added successfully!');
        fetchMovies(); //Atualiza Lista de Filmes
    } catch (error) {
        console.error('Error adding movie:', error);
        alert('Failed to add movie. Please try again.');
    }
});

//Deletar Filme
async function deleteMovie(id) {
    try {
        await fetch(`${apiUrl}/movies/${id}`, {
            method: 'DELETE'
        });
        fetchMovies(); //Atualizar Filme
    } catch (error) {
        console.error('Error deleting movie:', error);
    }
}

//Busca filmes já existentes ao carregar a página
fetchMovies();
