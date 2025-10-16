import json
from app import create_app, db
from models.bank_model import Banks, BankInfo
import os

app = create_app()

# paths to JSON files
offers_file_path = os.path.join(os.path.dirname(__file__), "data", "bank_offers.json")
banks_file_path = os.path.join(os.path.dirname(__file__), "data", "list_of_banks.json")

# Load bank offers from JSON
with open(offers_file_path) as f:
    offers = json.load(f)

# Load bank info from JSON
with open(banks_file_path) as f:
    banks_info = json.load(f)['banks'] # this is different to the one above because this json has a key "banks" at the start

with app.app_context():
    db.create_all()  # create tables if not exists

    # populate bank offers db
    # Get all current bank_ids from the JSON
    new_bank_ids = [offer["bank_id"] for offer in offers]

    for offer in offers:
        existing = Banks.query.filter_by(bank_id=offer["bank_id"]).first()

        if existing:
            # Update existing record
            existing.bank_name = offer["bank_name"]
            existing.min_deposit = offer["deposit"]
            existing.min_direct_debits = offer["direct_debits"]
            existing.switch_bonus = offer.get("bonus", None)
            existing.excludes = json.dumps(offer.get("excludes", []))
            existing.is_active = offer.get("is_active", True)
        else:
            # Add new record
            bank_offer = Banks(
                bank_id=offer["bank_id"],
                bank_name=offer["bank_name"],
                min_deposit=offer["deposit"],
                min_direct_debits=offer["direct_debits"],
                switch_bonus=offer.get("bonus", None),
                excludes=json.dumps(offer.get("excludes", [])),
                is_active=offer.get("is_active", True)
            )
            db.session.add(bank_offer)

    # populate bank info db
    for bank in banks_info:
        existing = BankInfo.query.filter_by(id=bank["id"]).first()

        if existing:
            existing.name = bank["name"]
            existing.logo = bank("logo") if "logo" in bank else None

        else:
            bank_entry = BankInfo(
                id=bank["id"],
                name=bank["name"],
                logo=bank["logo"] if "logo" in bank else None
            )
            db.session.add(bank_entry)


    db.session.commit()

    print("Database updated successfully.")