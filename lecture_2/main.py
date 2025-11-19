# Step 1: create function generate_profile
from datetime import datetime


def generate_profile(age):
    """
       Determines the life stage of a person based on their age.

       :param int age: The age of the person in years.
       :return: A string indicating the person's life stage:
           - "Child" (0-12 years)
           - "Teenager" (13-19 years)
           - "Adult" (20 years and older)
           - "Unknown" (invalid input, e.g., negative age)
       :rtype: str
       """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"

# Step 2: greeting and getting data from the user
print("Welcome to mini profile generator! ")
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")

try:
    birth_year = int(birth_year_str)
except ValueError:
    print("Incorrect input")
    exit()

# get the current year automatically
current_year = datetime.now().year
current_age = current_year - birth_year

# list hobbies
hobbies = []

while True:
    hobby_input = input("Enter a favorite hobby or type 'stop': ").strip()
    if hobby_input.lower() == 'stop':
        break
    if hobby_input:  # checking that the input is not empty
        hobbies.append(hobby_input)

# Step 3: create user_profile
life_stage = generate_profile(current_age)

# dictionary with initial key-value pairs
user_profile = {
    'name': user_name,
    'age': current_age,
    'stage': life_stage,
    'hobbies': hobbies
}

# Step 4: output
print("\n--- Profile Summary: ---")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life stage: {user_profile['stage']}")

if not user_profile['hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")