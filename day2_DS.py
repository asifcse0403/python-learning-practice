# claim_id = "CLM-1234"
# cust_age = 45
# claim_amount = 15000.00
# is_approved = True
# print(f"Claim {claim_id} for customer aged {cust_age} with amount ${claim_amount} has been approved: {is_approved}")

# statuses = ["submitted", "under review", "approved", "rejected"]
# print("First status:", statuses[0])
# print("Last status:", statuses[-1])

# statuses.append("paid")
# print("Total statuses:" , len(statuses))


Claim = {
    "claim_id" : "CLM=1001",
    "Policy_Holder" : "Shaik Asif",
    "Amount" : 15000.00,
    "status" : "Under Review"
}

print("Customer : ", Claim["Policy_Holder"])
Claim["status"] = "Approved"
Claim["Approved_by"] = "Manager"
print("Updated Claim : ", Claim)

