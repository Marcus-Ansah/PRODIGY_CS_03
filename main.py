import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length < 8:
        return "Weak: Password should be at least 8 characters long."
    elif not (has_upper and has_lower):
        return "Weak: Password should contain both uppercase and lowercase letters."
    elif not has_digit:
        return "Weak: Password should contain at least one digit."
    elif not has_special:
        return "Moderate: Consider adding special characters for increased security."
    else:
        return "Strong: Password meets all criteria for strength."


print("Password Strength Checker")
password = input("Enter your password to assess: ")
strength_feedback = check_password_strength(password)
print(strength_feedback)

