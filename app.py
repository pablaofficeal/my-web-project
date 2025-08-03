from flask import Flask
from config import Config
from models import db
from routers.home import home_host


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(home_host)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)