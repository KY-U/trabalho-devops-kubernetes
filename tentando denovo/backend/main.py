
import os
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'root'),
    'host': os.getenv('DB_HOST', 'mysql_database'),
    'database': os.getenv('DB_NAME', 'catalogo')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title, release_year, description FROM movies")
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')
    release_year = data.get('release_year')
    description = data.get('description')

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO movies (title, release_year, description) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, release_year, description))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Movie added successfully!"}), 201

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM movies WHERE id = %s"
    cursor.execute(query, (movie_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Movie removed successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)