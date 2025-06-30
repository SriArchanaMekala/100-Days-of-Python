try:
    age = int(input("How old are you?"))
except:
    print("You have typed an invalid number. Please try again using a numerical response such as 15.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
