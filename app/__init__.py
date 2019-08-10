from flask import Flask

app = Flask(__name__)
app.debug = True

from app.main import main as main_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
