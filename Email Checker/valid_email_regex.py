import re

# Email validation regex pattern
email_condition = r"^[a-z]+[._]?[a-z0-9]+@[a-z]+\.[a-z]{2,3}$"

# Input email and strip leading/trailing spaces
email = input("Enter email: ").strip()

# Check email validity using regex
if re.search(email_condition, email):
    print("✅ Success: Email address is valid!")
else:
    print("❌ Error: Email address is invalid! Please check the format.")
