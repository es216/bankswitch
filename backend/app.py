from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models.bank_model import db
from routes.banks import banks_bp
from routes.eligibility import eligibility_bp
from routes.list_of_banks import list_of_banks_bp
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    DB_URL = os.getenv("DB_URL", "sqlite:///banks.db")

    if DB_URL.startswith("postgres://"):
        DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(banks_bp)
    app.register_blueprint(eligibility_bp)
    app.register_blueprint(list_of_banks_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

