# Project 3: Phishing Awareness Analyzer
suspicious_words = [
    "urgent",
    "click here",
    "verify your account",
    "winner",
    "free",
    "password",
    "bank account",
    "suspended",
    "confirm your",
    "act now",
    "limited time",
    "you have been selected",
    "dear user",
    "login immediately",
    "update your information"
]

# These are fake/suspicious link patterns

suspicious_links = [
    "amaz0n",
    "paypa1",
    "g00gle",
    "micros0ft",
    "faceb00k",
    "login-update",
    "secure-verify",
    "account-confirm",
    "bit.ly",
    "tinyurl",
    "http://",
]

# ANALYZE FUNCTION (This function checks the message)

def analyze_message(message):

    # Convert message to lowercase for easy checking
    message_lower = message.lower()

    # We will store all red flags found here
    red_flags = []

    # We will count how many problems we find
    score = 0

    print("")
    print("=" * 50)
    print("   ANALYZING YOUR MESSAGE...")
    print("=" * 50)

    # ---- CHECK 1: Look for suspicious words ----
    print("")
    print("  STEP 1: Checking for suspicious words...")

    for word in suspicious_words:
        if word in message_lower:
            red_flags.append("Suspicious word found: '" + word + "'")
            score = score + 1

    # ---- CHECK 2: Look for fake links ----
    print("  STEP 2: Checking for suspicious links...")

    for link in suspicious_links:
        if link in message_lower:
            red_flags.append("Suspicious link found: '" + link + "'")
            score = score + 2

    # ---- CHECK 3: Check for urgency + action combo ----
    print("  STEP 3: Checking for urgency tactics...")

    if "urgent" in message_lower or "immediately" in message_lower:
        if "click" in message_lower or "login" in message_lower:
            red_flags.append("URGENCY TACTIC: Forcing user to click quickly!")
            score = score + 2

    # ---- CHECK 4: Asking for personal info ----
    print("  STEP 4: Checking for personal info requests...")

    if "password" in message_lower or "credit card" in message_lower:
        red_flags.append("DANGEROUS: Asking for password or credit card!")
        score = score + 3

    # ---- SHOW ALL RED FLAGS ----
    print("")
    print("=" * 50)
    print("  SCAN RESULTS:")
    print("=" * 50)

    if len(red_flags) == 0:
        print("  No red flags found!")
    else:
        print("  Red Flags Found:")
        for flag in red_flags:
            print("  ⚠️  " + flag)

    # ---- FINAL VERDICT ----
    print("")
    print("  Total Danger Score : " + str(score))

    if score == 0:
        print("  Verdict           : ✅ SAFE - No threats detected")
        print("  Action             : Close - Nothing suspicious")

    elif score <= 3:
        print("  Verdict           : ⚠️  SUSPICIOUS - Be careful!")
        print("  Action             : Warn User - Do not click any links")

    else:
        print("  Verdict           : 🚨 DANGEROUS - This is PHISHING!")
        print("  Action             : Block & Escalate - Report immediately!")

    print("=" * 50)
    print("")

#               MAIN PROGRAM

print("=" * 50)
print("   DecodeLabs Phishing Awareness Analyzer")
print("   Batch 2026 - Cybersecurity Project 3")
print("=" * 50)
print("")
print("  This tool analyzes messages for phishing")
print("  Red Flags, suspicious words, and fake links.")
print("")

while True:

    print("What do you want to do?")
    print("  1 - Analyze a message")
    print("  2 - See example phishing messages")
    print("  3 - Exit")
    print("")

    choice = input("Enter your choice (1, 2 or 3): ")
    print("")

    # ---- ANALYZE MESSAGE ----
    if choice == "1":
        print("Paste your message below.")
        print("Press ENTER twice when done.")
        print("")
        user_message = input("Message: ")
        analyze_message(user_message)

    # ---- SHOW EXAMPLES ----
    elif choice == "2":

        print("=" * 50)
        print("  EXAMPLE PHISHING MESSAGES:")
        print("=" * 50)
        print("")
        print("  Example 1 (DANGEROUS):")
        print("  'Dear User! Your bank account is suspended!")
        print("   Click here urgently: http://amaz0n-login.com'")
        print("")
        print("  Example 2 (SUSPICIOUS):")
        print("  'Congratulations! You are a winner!")
        print("   Claim your free prize now!'")
        print("")
        print("  Example 3 (SAFE):")
        print("  'Hi Abdullah, meeting is at 3pm tomorrow.'")
        print("")

    # ---- EXIT ----
    elif choice == "3":
        print("  Stay Alert! Stay Safe! — Hashaam From DecodeLabs")
        print("")
        break

    # ---- WRONG INPUT ----
    else:
        print("  Wrong choice! Enter 1, 2 or 3")
        print("")