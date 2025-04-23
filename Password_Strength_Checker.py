import re

def check_strength(Password):
    Length = len(Password) >= 8  # Use >= instead of ≥
    UpperCase = re.search(r"[A-Z]", Password)
    LowerCase = re.search(r"[a-z]", Password)
    Digit = re.search(r"[0-9]", Password)
    Special = re.search(r"[!@#$%^&*(),.?\":{}|]", Password)
    
    if all([Length, UpperCase, LowerCase, Digit, Special]):
        return "Strong"
    elif Length and (UpperCase or LowerCase) and Digit:
        return "Moderate"
    else:
        return "Weak"

pwd = input("Enter a password to check its strength: ")
print(f"Password Strength: {check_strength(pwd)}")
