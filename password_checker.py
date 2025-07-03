import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Display result
    print(f"\nPassword Strength Score: {strength}/5")
    if strength == 5:
        print("✅ Strong password!")
    else:
        print("⚠️ Weak password. Suggestions:")
        for tip in feedback:
            print("- " + tip)

# Example usage
user_input = input("Enter a password to test: ")
check_password_strength(user_input)
