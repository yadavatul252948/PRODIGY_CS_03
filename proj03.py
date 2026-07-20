import string

password = input("Enter your password: ")

length = len(password) >= 8
uppercase = any(c.isupper() for c in password)
lowercase = any(c.islower() for c in password)
digit = any(c.isdigit() for c in password)
special = any(c in string.punctuation for c in password)

score = sum([length, uppercase, lowercase, digit, special])

print("\nPassword Analysis:")

if length:
    print("✓ Length is at least 8 characters")
else:
    print("✗ Password should be at least 8 characters long")

if uppercase:
    print("✓ Contains uppercase letter")
else:
    print("✗ Missing uppercase letter")

if lowercase:
    print("✓ Contains lowercase letter")
else:
    print("✗ Missing lowercase letter")

if digit:
    print("✓ Contains a number")
else:
    print("✗ Missing a number")

if special:
    print("✓ Contains a special character")
else:
    print("✗ Missing a special character")

print("\nPassword Strength:")

if score == 5:
    print("Strong Password 💪")
elif score >= 3:
    print("Moderate Password 👍")
else:
    print("Weak Password ❌")