from flask import Blueprint, jsonify
from data.bank_offers import bank_offers

## create blueprint
banks_bp = Blueprint("banks", __name__)

@banks_bp.route("/banks", methods=["GET"])
def get_banks():
    return jsonify(bank_offers)