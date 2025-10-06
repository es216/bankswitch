from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.banks import banks_bp
from routes.eligibility import eligibility_bp
from routes.list_of_banks import list_of_banks_bp


app = Flask(__name__)
CORS(app)

from models.bank_model import db

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(banks_bp)
app.register_blueprint(eligibility_bp)
app.register_blueprint(list_of_banks_bp)

if __name__ == "__main__":
    app.run(debug=True)

