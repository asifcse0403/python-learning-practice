base_salary = 65000
bonus = 8500
Total_pay = base_salary + bonus
print(f"Total Compensation is : ${Total_pay}")

skills = ["Python", "SQL", "Git"]
skills.append("FastAPI")
print("The second skill on the list is : ", skills[1])
print("Total no.of skills in the list are : ", len(skills))


health_claim = {
    "id": "HC-1001",
    "hospital" : "Apollo Hospital",
    "bill_amount" : 45000,
    "is_settled" : False
}

health_claim["is_settled"] = True
health_claim["settlement_date"] = "2024-11-22"

print("Final Health Claim : ", health_claim)
