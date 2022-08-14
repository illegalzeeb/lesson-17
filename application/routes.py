from flask import current_app as app, request
from flask_restx import Api, Namespace, Resource
from application.models import db
from application import models, schema

api: Api = app.config['api']
movies_ns: Namespace = api.namespace('movies')

movies_schema = schema.Movie(many=True)
movie_schema = schema.Movie()


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies_query = db.session.query(models.Movie)

        args = request.args

        director_id = args.get('director_id')

        if director_id is not None:
            movies_query = movies_query.filter(models.Movie.director_id == director_id)

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies_query = movies_query.filter(models.Movie.genre_id == genre_id)

        movies = db.session.query(models.Movie).all()

#        movies = db.session.query(models.Movie).all()
        return movies_schema.dump(movies), 200


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(selfself, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()
        if movie is None:
            return{ }, 404
        return movie_schema.dump(movie), 200
