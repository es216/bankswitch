# function to check eligibility criteria - returns list of eligible and ineligible banks
def eligible_switch(bank_offers, user_input):
     ineligible = []
     eligible = []
     user_bank = user_input["bank"]
     user_direct_debits = user_input["direct_debits"]
     user_deposit = user_input["deposit"]

     for offer in bank_offers:
        exclusions = offer["excludes"]
        if user_bank in exclusions:
            ineligible.append(offer["name"])
        min_deposit = offer["min_deposit"]
        if user_deposit < min_deposit:
            if offer["name"] not in ineligible:
                ineligible.append(offer["name"])
        direct_debits = offer["min_direct_debits"]
        if user_direct_debits < direct_debits:
            if offer["name"] not in ineligible:
                ineligible.append(offer["name"])

     for offer in bank_offers:
        bank = offer["name"]
        if bank not in ineligible:
            eligible.append(bank)

     return {"eligible": eligible, "ineligible": ineligible}