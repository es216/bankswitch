import json
from flask import Blueprint, jsonify

## create blueprint
banks_bp = Blueprint("banks", __name__)

## API: returns all bank offers
@banks_bp.route("/banks", methods=["GET"])
def get_banks():
    with open("data/bank_offers.json") as f:
        bank_offers = json.load(f)
    return jsonify(bank_offers)