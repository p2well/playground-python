age = int(input("How old are you?\n"))

decades = age // 10  # integer division called floor division
years = age % 10  # remainder called modulus

print(f"You are {decades} decades and {years} years old.")
