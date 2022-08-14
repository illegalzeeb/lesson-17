from marshmallow import Schema, fields

#"""
#Сериализация
#"""


class Movie(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
#    genre = db.relationship("Genre")
    director_id = fields.Int()
#    director = db.relationship("Director")


class Director(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Genre(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()