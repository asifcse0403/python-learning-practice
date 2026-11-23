# claim_amount = 75000

# if claim_amount > 50000:
#    print("High value claim : Route to Senio Auditor")
# elif claim_amount > 10000:
#    print("Medium value claim : Standard review")
# else:
#    print("Low value claim : Auto-approved")

claims = [
    {"id" : "CLM-101", "amount" : 8000, "status" : "Pending"},
    {"id" : "CLM-102", "amount" : 65000, "status" : "Pending"},
    {"id" : "CLM-103", "amount" : 22000, "status" : "Rejected"}
]

for claim in claims:
    print(f"Checking {claim['id']} for amount ${claim["amount"]}")

    if claim["status"] == "Rejected":
        print(" --> Action : Send rejection email")
    elif claim["amount"] > 50000:
        print(" --> Action : Flag for manual audit") 
    else:
        print(" --> Action : Auto-approved")
