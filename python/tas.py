import random
user_answer = input("do you whant a random number? (y/n) : ")

if user_answer == "y":
    print(random.randint(1,6))
elif user_answer == "n":
    print("ok bye")
else:
    print("are you ok? just answer y or n")