import random
amount = input("How many dice do you want? : ")
amount = int(amount)
sides = input("How many sides does the die have? : ")
sides = int(sides)
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Dice rolling...")
    for z in range(amount):
       print(f"Die number",z+1, " = ",random.randint(1, sides)) 
    else:
       roll_again = input("Roll again? (yes / y) : ")
