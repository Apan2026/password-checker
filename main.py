import re

print("=== Password Strength Checker ===")

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Uppercase check
if re.search(r"[A-Z]", password):
    strength += 1

# Lowercase check
if re.search(r"[a-z]", password):
    strength += 1

# Number check
if re.search(r"[0-9]", password):
    strength += 1

# Special character check
if re.search(r"[@$!%*?&]", password):
    strength += 1

# Result
if strength <= 2:
    print("Weak Password")

elif strength == 3 or strength == 4:
    print("Medium Password")

else:
    print("Strong Password")
