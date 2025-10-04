from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.banks import banks_bp
from routes.eligibility import eligibility_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(banks_bp)
app.register_blueprint(eligibility_bp)

# static user input goes here
user_input = {
    "bank": "Bank A",
    "direct_debits": 2,
    "deposit": 2200
}

## prints for debugging
     ##print("Ineligible banks: " + str(ineligible))
     ##print("Eligible banks: " + str(eligible))
## call function for debugging
##eligible_switch(bank_offers, user_input)

if __name__ == "__main__":
    app.run(debug=True)

