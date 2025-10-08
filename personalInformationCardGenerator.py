name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("What’s your favorite hobby?")
is_student = input("Are you a student? (yes/no): ").strip().lower() == 'yes'
height = float(input("Enter your height (e.g., 1.75): "))

birthYear = 2025 - age
heightToCm = height * 100
if age >= 18:
    is_adult = True
else:
    is_adult = False

if is_student and age <= 25:
    is_young_student = True
else:
    is_young_student = False


print("=== Personal Information Card ===")
print("Name:", name.upper())
print(f"Age: {age} years")
print(f"Born Around: {birthYear}")
print("Favorite Hobby:", hobby.capitalize())
print("Height:", f"{heightToCm} cm")
print("Student: ", is_student)
print("Status: ", is_adult)
print("Young Student:", is_young_student)


