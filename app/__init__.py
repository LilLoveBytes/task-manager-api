from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# db and migrae give access to db operations
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #hides a warning 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #sets connection string
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:postgres@localhost:5432/task_manager_api'

    #connects db, migrate to flask
    db.init_app(app)
    migrate.init_app(app, db)

    #register bp
    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app
