from flask import Blueprint, request, jsonify
from data.bank_offers import bank_offers
from services.eligibility_logic import eligible_switch

## blueprint
eligibility_bp = Blueprint("eligibility", __name__)

## API: eligibility checker
@eligibility_bp.route("/eligible", methods=["POST"])
def check_eligibility():
    user_data = request.get_json()
    result = eligible_switch(bank_offers, user_data)
    return jsonify(result)

