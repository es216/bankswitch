from flask import Blueprint, request, jsonify
from models.bank_model import Banks, BankInfo, db
from services.live_offers_logic import get_live_offers

## blueprint
live_offers_bp = Blueprint("live_offers", __name__)

## API: returns live offers
@live_offers_bp.route("/live_offers", methods=["GET"])
def check_live_offers():

    # load bank switch offer data from the database
    banks = Banks.query.all()
    bank_offers = [bank.to_dict() for bank in banks]

    #load bank info data from the database to get logos
    list_of_banks = BankInfo.query.all()
    bank_info = [bank.to_dict() for bank in list_of_banks]

    result = get_live_offers(bank_offers, bank_info)
    return jsonify(result)