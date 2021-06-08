from sqlalchemy.orm import backref
from werkzeug.exceptions import default_exceptions
from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))


class User(db.Model, UserMixin):

     id = db.Column(db.Integer(), primary_key=True)
     username = db.Column(db.String(32), unique=True, nullable=False)
     password_hash = db.Column(db.String(64), nullable=False)
     email_address = db.Column(db.String(32), nullable=False, unique=True)
     budget = db.Column(db.Integer(), nullable=False, default=1000)
     items = db.relationship('item', backref='owned_user', lazy=True)

     @property
     def password(self):
         return self.password
    
     @password.setter
     def password(self, plain_text_password):
        self.password_hash = bcrypt.get_password_hash(plain_text_password).decode('utf-8')

     def check_password_correction(self, attempted_password):
         return bcrypt.check_password_hash(self.password_hash, attempted_password)


class item(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'item {self.name}'




