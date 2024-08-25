from flask import Flask, jsonify, request
from flask_cors import CORS

#Códigos de status HTTP:
#400 (Bad Request)
#200 (OK)
app = Flask(__name__)
CORS(app)

#BD na memória para simplicidade
movies = []

@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/api/movies', methods=['POST'])
def add_movie():
    movie = request.json
    if 'title' not in movie or 'year' not in movie:
        return jsonify({'error': 'Invalid movie data'}), 400
    movies.append(movie)
    return jsonify(movie), 201

@app.route('/api/movies/<string:title>', methods=['DELETE'])
def delete_movie(title):
    global movies
    movies = [movie for movie in movies if movie['title'] != title]
    return jsonify({'message': 'Movie deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')