# static list of banks
bank_offers = [ 
    {
        "bank": "Bank A",
        "bonus": 185,
        "direct_debits": 2,
        "deposit": 1000,
        "excludes": ["Bank A", "Bank C"] # should always be a list, even if one one bank
    },
    {
        "bank": "Bank B",
        "bonus": 120,
        "direct_debits": 2,
        "deposit": 500,
        "excludes": ["Bank B"]
    },
    {
        "bank": "Bank C",
        "bonus": 200,
        "direct_debits": 0,
        "deposit": 1300,
        "excludes": ["Bank C"]
    },
    {
        "bank": "Bank D",
        "bonus": 145,
        "direct_debits": 1,
        "deposit": 200,
        "excludes": ["Bank D", "Bank B"]
    },
    {
        "bank": "Bank E",
        "bonus": 230,
        "direct_debits": 0,
        "deposit": 2000,
        "excludes": ["Bank E"]
    },
]
