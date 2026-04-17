# ENCRYPT FUNCTION locks the message
def encrypt(message, shift):

    # We will store our encrypted letters here
    encrypted_message = ""

    # Go through each letter one by one
    for letter in message:

        # Check if it is a CAPITAL letter (A to Z)
        if letter.isupper():

            # Step 1: Convert letter to number (A=0, B=1, C=2...)
            letter_number = ord(letter) - 65

            # Step 2: Add the shift key
            shifted_number = letter_number + shift

            # Step 3: Use % 26 so it wraps around (Z goes back to A)
            wrapped_number = shifted_number % 26

            # Step 4: Convert number back to letter
            new_letter = chr(wrapped_number + 65)

            # Add this new letter to our result
            encrypted_message = encrypted_message + new_letter

        # Check if it is a small letter (a to z)
        elif letter.islower():

            # Same steps but for small letters (a=97)
            letter_number = ord(letter) - 97
            shifted_number = letter_number + shift
            wrapped_number = shifted_number % 26
            new_letter = chr(wrapped_number + 97)

            encrypted_message = encrypted_message + new_letter

        # If it is a space or symbol — keep it as it is
        else:
            encrypted_message = encrypted_message + letter

    return encrypted_message


# ------------------------------------------
# DECRYPT FUNCTION
# This function unlocks the message
# ------------------------------------------

def decrypt(message, shift):

    decrypted_message = ""

    for letter in message:

        if letter.isupper():
            letter_number = ord(letter) - 65
            shifted_number = letter_number - shift
            wrapped_number = shifted_number % 26
            new_letter = chr(wrapped_number + 65)
            decrypted_message = decrypted_message + new_letter

        elif letter.islower():
            letter_number = ord(letter) - 97
            shifted_number = letter_number - shift
            wrapped_number = shifted_number % 26
            new_letter = chr(wrapped_number + 97)
            decrypted_message = decrypted_message + new_letter

        else:
            decrypted_message = decrypted_message + letter

    return decrypted_message

#               MAIN PROGRAM

print("============================================")
print("   DecodeLabs Encryption & Decryption Tool")
print("   Batch 2026 - Cybersecurity Project 2")
print("============================================")
print("")

while True:

    print("What do you want to do?")
    print("  1 - Encrypt a message")
    print("  2 - Decrypt a message")
    print("  3 - Exit")
    print("")

    choice = input("Enter your choice (1, 2 or 3): ")
    print("")

    # ---- ENCRYPT ----
    if choice == "1":

        user_message = input("Enter your message to encrypt: ")
        user_shift = int(input("Enter shift key (example: 3): "))

        result = encrypt(user_message, user_shift)

        print("")
        print("============================================")
        print("  Original Message  : " + user_message)
        print("  Shift Key Used    : " + str(user_shift))
        print("  Encrypted Message : " + result)
        print("============================================")
        print("")

    # ---- DECRYPT ----
    elif choice == "2":

        user_message = input("Enter encrypted message to decrypt: ")
        user_shift = int(input("Enter shift key (example: 3): "))

        result = decrypt(user_message, user_shift)

        print("")
        print("============================================")
        print("  Encrypted Message : " + user_message)
        print("  Shift Key Used    : " + str(user_shift))
        print("  Decrypted Message : " + result)
        print("============================================")
        print("")

    # ---- EXIT ----
    elif choice == "3":
        print("  Stay Secure! — DecodeLabs")
        print("")
        break

    # ---- WRONG INPUT ----
    else:
        print("  Wrong choice! Please enter 1, 2 or 3")
        print("")