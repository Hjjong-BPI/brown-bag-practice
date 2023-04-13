def calculate_age(birthyear):
    return 2023 - birthyear

print("What is your name?")
name = input()

print("What year were you born?")
birthyear = input()
birthyear = int(birthyear)

age = calculate_age(birthyear)

print(f"Hello {name}, you are {age} years old!")
