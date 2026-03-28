# Smart Input Program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorize age
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

# Print personalized message
print(f"\nHello {name}! 👋")
print(f"You are a {category} who loves {hobby}. Keep enjoying!")
