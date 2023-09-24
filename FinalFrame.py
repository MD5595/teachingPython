import random
import math

x = input("Enter your name")
user_num = int(input("Enter a number from 1 to 100"))

if user_num > 100 or user_num < 1:
    print("No")

num1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
animal = random.choice(["Cow", "Pig", "Sheep", "Dog", "Whale"])


your_random_password = str(animal) + str(num1)
print(your_random_password)
