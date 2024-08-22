from flask import Flask, request, jsonify
from models import db, Movie

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/catalogo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{'id': movie.id, 'title': movie.title, 'year': movie.year} for movie in movies])

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    new_movie = Movie(title=data['title'], year=data['year'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'Movie added!'}), 201

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie deleted!'})
    return jsonify({'message': 'Movie not found!'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)