incoming_claims = [
    {"claim_id" : "C-01", "type" : "Medical", "amount" : 12000, "has_receipt" : True},
    {"claim_id" : "C-02", "type" : "Property", "amount" : 85000, "has_receipt" : True},
    {"claim_id" : "C-03", "type" : "Medical", "amount" : 4500, "has_receipt" : False},
    {"claim_id" : "C-04", "type" : "Property", "amount" : 30000, "has_receipt" : True}
]

approved_count = 0
for claim in incoming_claims:
    if claim["has_receipt"] == False:
        claim["label"] = "Missing Documents"
    elif claim["amount"] > 50000:
        claim["label"] = "Large Claim - Audit Required"
    else:
        claim["label"] = "Standard Claim - Auto-approved"
        approved_count += 1
    print(f"Claim : {claim['claim_id']} -> ({claim['type']}) -> {claim['label']}")

print(f"Total Approved Claims : {approved_count}")
