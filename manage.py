# coding:utf8
from app import app
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

if __name__ == "__main__":
    app.run()