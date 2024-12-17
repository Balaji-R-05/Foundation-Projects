# Input the email and remove any leading/trailing spaces
email = input("Enter your Email: ").strip()

# Initialize validation flags
has_Space = False
has_Uppercase = False
has_InvalidChar = False

# Start validation
if len(email) >= 6:  # Check minimum length
    if email[0].isalpha():  # Check if email starts with an alphabet
        if ("@" in email) and (email.count("@") == 1):  # Check for exactly one '@'
            if email[-4] == "." or email[-3] == ".":  # Check valid domain ending
                # Check each character in the email
                for char in email:
                    if char.isspace():  # Check for spaces
                        has_Space = True
                    elif char.isalpha():  # Check for uppercase letters
                        if char.isupper():
                            has_Uppercase = True
                    elif char.isdigit() or char in ['@', '_', '.']:  # Allowed special characters
                        continue
                    else:  # Invalid characters
                        has_InvalidChar = True

                # Display appropriate error messages
                if has_Space:
                    print("❌ Error: Email address cannot contain spaces.")
                if has_Uppercase:
                    print("❌ Error: Email address cannot contain uppercase letters.")
                if has_InvalidChar:
                    print("❌ Error: Email address contains invalid characters. Only '@', '.', and '_' are allowed.")
                if not (has_Space or has_Uppercase or has_InvalidChar):
                    print("✅ Success: Email address is valid!")
            else:
                print("❌ Error: Email address must end with a valid domain (e.g., '.com', '.org', '.in').")
        else:
            print("❌ Error: Email address must contain exactly one '@' symbol.")
    else:
        print("❌ Error: Email address must start with an alphabet (a-z or A-Z).")
else:
    print("❌ Error: Email address must be at least 6 characters long.")
