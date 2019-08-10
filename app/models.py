# coding:utf8
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime
from flask import Flask
import pymysql

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wma8:1234@127.0.0.1:3306/dev'
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)


class Homework(db.Model):
    __tablename__ = "homework"
    id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.String(100), unique=True)
    time = db.Column(db.DateTime, index=True, default=datetime.now)
    homework_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Work %r>' % self.work


# User
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    homework = db.relationship('Homework', backref='user')

    def __repr__(self):
        return '<User %r> ' % self.username


# auth
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Auth %r>" % self.name


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    roleid = db.Column(db.Integer)  # 0 stands for admin, 1 for user
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Admins %r>' % self.username


if __name__ == "__main__":
    pass
    # db.create_all()
    # from werkzeug.security import generate_password_hash
    #
    # admin = Admin(
    #     name="admin",
    #     pwd=generate_password_hash("1234qwer"),
    #     roleid=1
    # )
    # db.session.add(admin)
    # db.session.commit()
