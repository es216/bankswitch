import json
from app import create_app, db
from models.bank_model import Banks
import os

app = create_app()

file_path = os.path.join(os.path.dirname(__file__), "data", "bank_offers.json")

with open(file_path) as f:
    offers = json.load(f)

with app.app_context():
    db.create_all()  # create tables if not exists

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
            bank = Banks(
                bank_id=offer["bank_id"],
                bank_name=offer["bank_name"],
                min_deposit=offer["deposit"],
                min_direct_debits=offer["direct_debits"],
                switch_bonus=offer.get("bonus", None),
                excludes=json.dumps(offer.get("excludes", [])),
                is_active=offer.get("is_active", True)
            )
            db.session.add(bank)

    db.session.commit()

    print("Database updated successfully.")