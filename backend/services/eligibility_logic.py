import os

# function to check eligibility criteria - returns list of eligible and ineligible banks
def eligible_switch(bank_offers, bank_info, user_input):
    ineligible = []
    eligible = []
    user_bank_id = int(user_input["bank"]) ## must be int or won't match with int in excludes list
    user_direct_debits = user_input["direct_debits"]
    user_deposit = user_input["deposit"]
    live_bank_offers = [offer for offer in bank_offers if offer["is_active"]]
    sum_bonus = 0
    LOGO_TOKEN = os.getenv("LOGO_DEV_KEY") ## get logo token from env

## check each bank offer against user criteria to create list of ineligible banks    
    for offer in live_bank_offers:
        exclusions = offer["excludes"]
        if user_bank_id in exclusions:
            ineligible.append(offer["bank_name"])
        min_deposit = offer["min_deposit"]
        if user_deposit < min_deposit:
            if offer["bank_name"] not in ineligible:
                ineligible.append(offer["bank_name"])
        direct_debits = offer["min_direct_debits"]
        if user_direct_debits < direct_debits:
            if offer["bank_name"] not in ineligible:
                ineligible.append(offer["bank_name"])

## create list of dicts of eligible banks by excluding ineligible ones
    for offer in live_bank_offers:
        bank_id = offer["bank_id"]
        bank_name = offer["bank_name"]
        min_deposit = offer["min_deposit"]
        direct_debits = offer["min_direct_debits"]
        switch_bonus = offer["switch_bonus"]

        logo = next((bank["logo"] for bank in bank_info if bank["id"] == bank_id), None)

        if bank_name not in ineligible:
            logo_with_token = f"{logo}{LOGO_TOKEN}" if logo and LOGO_TOKEN else logo

            eligible.append({
                "logo": logo_with_token,
                "bank_name": bank_name,
                "min_deposit": min_deposit,
                "min_direct_debits": direct_debits,
                "switch_bonus": switch_bonus
                })


## sum up the switch bonuses for eligible banks
    for offer in eligible:
        sum_bonus += offer["switch_bonus"]

    
     

    return {"eligible": eligible, "ineligible": ineligible, "sum_bonus": sum_bonus}


## this would be better if it took into account if just customer, or switch bonus

## this is how you debug with print statements to the console: print("My print statement", flush=True)