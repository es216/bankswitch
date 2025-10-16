from flask import Blueprint, request, jsonify
from models.bank_model import Banks, BankInfo, db
from services.eligibility_logic import eligible_switch

## blueprint
eligibility_bp = Blueprint("eligibility", __name__)

## API: eligibility checker
@eligibility_bp.route("/eligible", methods=["POST"])
def check_eligibility():
 
    # get user data from API
    user_data = request.get_json()

    # load bank switch offer data from the database
    banks = Banks.query.all()
    bank_offers = [bank.to_dict() for bank in banks]

    #load bank info data from the database to get logos
    list_of_banks = BankInfo.query.all()
    bank_info = [bank.to_dict() for bank in list_of_banks]


    result = eligible_switch(bank_offers, bank_info, user_data)
    return jsonify(result)
