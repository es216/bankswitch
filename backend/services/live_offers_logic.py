import os

#bank_offers is the list of offers
#bank_info is the list of banks with logo urls

def get_live_offers(bank_offers, bank_info):
    live_bank_offers = [offer for offer in bank_offers if offer["is_active"]]
    LOGO_TOKEN = os.getenv("LOGO_DEV_KEY") ## get logo token from env
    result = []
    sum_bonus = 0

    for offer in live_bank_offers:
        bank_id = offer["bank_id"]
        logo = next((bank["logo"] for bank in bank_info if bank["id"] == bank_id), None)
        bank_name = offer["bank_name"]
        min_deposit = offer["min_deposit"]
        direct_debits = offer["min_direct_debits"]
        switch_bonus = offer["switch_bonus"]

        sum_bonus += offer["switch_bonus"]
 
        logo_with_token = f"{logo}{LOGO_TOKEN}" if logo and LOGO_TOKEN else logo


        result.append({
            "logo": logo_with_token,
            "bank_name": bank_name,
            "min_deposit": min_deposit,
            "min_direct_debits": direct_debits,
            "switch_bonus": switch_bonus
        })


    return {"live_offers": result, "sum_bonus": sum_bonus}



