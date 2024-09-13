CREATE DATABASE IF NOT EXISTS catalogo;
USE catalogo;

CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_year INT NOT NULL,
    description TEXT
);

INSERT INTO movies (title, release_year, description) VALUES
('Inception', 2010, 'A skilled thief is given a chance at redemption if he can successfully perform inception: planting an idea into the target\'s subconscious.'),
('The Matrix', 1999, 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'),
('The Shawshank Redemption', 1994, 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
('The Godfather', 1972, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
('Pulp Fiction', 1994, 'The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.');
