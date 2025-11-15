from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models.bank_model import db
from routes.banks import banks_bp
from routes.eligibility import eligibility_bp
from routes.list_of_banks import list_of_banks_bp
from routes.live_offers import live_offers_bp
import os

def create_app():
    # instance_relative_config=True means Flask will use backend/instance/ for files
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Path to the local SQLite database inside instance/
    db_path = os.path.join(app.instance_path, "banks.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Ensure the instance/ folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Init DB + migrations
    db.init_app(app)
    Migrate(app, db)

    # Blueprints
    app.register_blueprint(banks_bp)
    app.register_blueprint(eligibility_bp)
    app.register_blueprint(list_of_banks_bp)
    app.register_blueprint(live_offers_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
