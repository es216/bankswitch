from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class Banks(db.Model):
    __tablename__ = 'bank_offers'
    
    id = db.Column(db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, nullable=False)
    bank_name = db.Column(db.String(50), nullable=False)
    min_deposit = db.Column(db.Integer, nullable=False)
    min_direct_debits = db.Column(db.Integer, nullable=False)
    switch_bonus = db.Column(db.Integer, nullable=True)
    excludes = db.Column(db.String, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'bank_id': self.bank_id,
            'bank_name': self.bank_name,
            'min_deposit': self.min_deposit,
            'min_direct_debits': self.min_direct_debits,
            'switch_bonus': self.switch_bonus,
            'excludes': json.loads(self.excludes) if self.excludes else [],
            'is_active': self.is_active
        }
    
