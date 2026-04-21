def check_password_strength(password):
    if " " in password:
        return "Invalid character: Passwords cannot contain spaces."
    if len(password) <= 6:
        return "Your password is Weak"
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    has_special = any(not i.isalnum() for i in password)
    score = 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1
    if score < 3:
        return "Your password is Weak"
    elif 3 <= score < 5:
        return "Your password is Medium"
    else:
        return "Your password is Strong"
password = input("Enter a password to check: ")
print(check_password_strength(password))