import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length check
    if len(password) < 8:
        print("\n" + "="*45)
        print("  Password : " + "*" * len(password))
        print("  Strength : WEAK")
        print("  Reason   : Too short! Minimum 8 characters.")
        print("="*45 + "\n")
        return

    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    # Rule 2: Uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add UPPERCASE letters (A-Z)")

    # Rule 3: Lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")

    # Rule 4: Digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add numbers (0-9)")

    # Rule 5: Special symbols
    special = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    if any(char in special for char in password):
        score += 2
    else:
        feedback.append("Add special symbols (!@#$%^&*)")

    # Rule 6: Common password check
    common = ["password", "123456", "password123", "admin",
              "qwerty", "letmein", "welcome", "monkey", "abc123"]
    if password.lower() in common:
        print("\n" + "="*45)
        print("  Password : " + "*" * len(password))
        print("  Strength : WEAK")
        print("  Reason   : Commonly leaked password!")
        print("="*45 + "\n")
        return

    # Result
    if score <= 2:
        strength = "WEAK"
        icon = "❌"
    elif score <= 4:
        strength = "MEDIUM"
        icon = "⚠️ "
    else:
        strength = "STRONG"
        icon = "✅"

    print("\n" + "="*45)
    print("  Password : " + "*" * len(password))
    print(f"  Score    : {score}/7")
    print(f"  Strength : {icon} {strength}")
    if feedback:
        print("  Improve  : " + " | ".join(feedback))
    else:
        print("  Status   : GATEKEEPER PASS ✔")
    print("="*45 + "\n")


# ── Main Program ──
print("="*45)
print("  🔐 DecodeLabs Password Strength Checker")
print("  Batch 2026 | Cybersecurity Project 1")
print("="*45 + "\n")

while True:
    user_input = input("Enter password (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("\n  Stay Secure! 🛡️  — DecodeLabs\n")
        break
    check_password_strength(user_input)