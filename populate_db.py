import json
from app import app, db
from models.bank_model import Banks
import os

file_path = os.path.join(os.path.dirname(__file__), "data", "bank_offers.json")

with open(file_path) as f:
    offers = json.load(f)

with app.app_context():
    db.create_all()  # create tables if not exists

    for offer in offers:
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