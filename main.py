Name = input("what's your name? ")
Age = int(input("What year were you born? "))
info = input("Please enter 3 hobbies you have separated by spaces:  ").split()

Age = 2026 - Age
print(f"Hello {Name}, you are {Age} years old and you love {info[0]} and {info[2]}, but you love {info[1]} most!")

