from sqlalchemy.orm import backref
from werkzeug.exceptions import default_exceptions
from market import db

class User(db.Model):

     id = db.Column(db.Integer(), primary_key=True),
     username = db.Column(db.String(32), unique=True, nullable=False),
     password_hash = db.Column(db.String(64), nullable=False),
     email_adress = db.Column(db.String(32), nullable=False, unique=True),
     budget = db.Column(db.Integer(), nullable=False, default=1000),
     items = db.relationship('item', backref='owned_user')

class item(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True),
    name = db.Column(db.String(50), nullable=False, unique=True),
    price = db.Column(db.Integer(), nullable=False),
    barcode = db.Column(db.String(12), nullable=False, unique=True),
    description = db.Column(db.String(1024), nullable=False, unique=True),
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'item {self.name}'




