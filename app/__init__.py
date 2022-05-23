from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)


from app import routes, models, modelSchema

if __name__ == '__main__':
    app.run(debug=True)