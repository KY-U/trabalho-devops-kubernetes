import os
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import pooling

app = Flask(__name__)
CORS(app)

db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'root'),
    'host': os.getenv('DB_HOST', 'mysql_database'),
    'database': os.getenv('DB_NAME', 'catalogo')
}

#pool de conexões para reutilizar conexões
connection_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_db_connection():
    try:
        return connection_pool.get_connection()
    except mysql.connector.Error as err:
        app.logger.error(f"Error connecting to database: {err}")
        return None

def handle_db_error(error):
    app.logger.error(f"Database error: {error}")
    return jsonify({"error": "Database error occurred"}), 500

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to database"}), 500
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, title, release_year, description FROM movies")
            movies = cursor.fetchall()
    except mysql.connector.Error as err:
        return handle_db_error(err)
    finally:
        conn.close()
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')
    release_year = data.get('release_year')
    description = data.get('description')

    if not title or not release_year or not description:
        return jsonify({"error": "All fields (title, release_year, description) are required"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to database"}), 500
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO movies (title, release_year, description) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, release_year, description))
            conn.commit()
            app.logger.info("Movie added: %s", title)
    except mysql.connector.Error as err:
        return handle_db_error(err)
    finally:
        conn.close()

    return jsonify({"message": "Movie added successfully!"}), 201

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to database"}), 500
    try:
        with conn.cursor() as cursor:
            query = "DELETE FROM movies WHERE id = %s"
            cursor.execute(query, (movie_id,))
            conn.commit()
            app.logger.info("Movie deleted with ID: %s", movie_id)
    except mysql.connector.Error as err:
        return handle_db_error(err)
    finally:
        conn.close()

    return jsonify({"message": "Movie removed successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)