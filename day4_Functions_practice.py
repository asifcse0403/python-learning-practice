def process_claim(claim_dict):
    try:
        amount = float(claim_dict["amount"])
        if amount <= 0:
            return "Invalid Amount"
        elif amount > 50000:
            return "Audit Required"
        else:
            return "Auto Approved"
        
    except (ValueError, TypeError, KeyError):
        return "Data Error : Check Claim Amount"

messy_claims = [
    {"id" : "C-01", "amount" : "15000"},
    {"id" : "C-02", "amount" : 75000},
    {"id" : "C-03", "amount" : "abc"},
    {"id" : "C-04", "wrong_key" : 5000}
]

for items in messy_claims:
    status = process_claim(items)
    print(f"Claim {items['id']} : {status}")