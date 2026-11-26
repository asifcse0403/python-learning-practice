def evaluate_claim(amount, has_receipt):
    try : 
        if not has_receipt:
            return "Missing Documents!"
        elif amount > 50000:
            return "Large Claim - Audit Required"
        else:
            return "Standard Claim - Auto Approved"
    except TypeError:
        print(f"Error! {amount} is not a valid number")
        return

result1 = evaluate_claim("abc", True)
result2 = evaluate_claim(80000, True)

print("Claim 1 : ", result1)
print("Claim 2 : ", result2)

