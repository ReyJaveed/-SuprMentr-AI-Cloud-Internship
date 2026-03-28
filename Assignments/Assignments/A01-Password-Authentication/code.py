import re

def check_strength(password):
    if len(password) < 8:
        return "Weak: Minimum 8 characters required"

    if not re.search("[a-z]", password):
        return "Weak: Add lowercase letters"

    if not re.search("[A-Z]", password):
        return "Weak: Add uppercase letters"

    if not re.search("[0-9]", password):
        return "Weak: Add numbers"

    if not re.search("[@#$%^&*]", password):
        return "Weak: Add special characters"

    return "Strong Password ✅"

def authenticate():
    correct_password = "Reya@123"
    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")
        print(check_strength(password))

        if password == correct_password:
            print("Access Granted 🔓")
            return
        else:
            attempts -= 1
            print(f"Wrong password! Attempts left: {attempts}")

    print("Access Denied ❌")

authenticate()
