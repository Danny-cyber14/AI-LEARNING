from math import *

"""
#basic value calculations
array = ["Dan", "fan" , "gan", "lan", "san", "kan"]
index = [1, 5, 4]
result = [array[i] for i in index]
print(result)

variable = input("Enter a number: ")
second_variable = input("Enter another number: ")
third_variable = int(variable) + int(second_variable)
message = "YOUR LUCKY NUMBER IS ".lower() + str(third_variable) + " CONGRATS\nTO YOU".upper()
print(message)


num = 3
num_2 = "6"
num_3 = num - int(num_2)
print(abs(num_3))


print(pow(9, 12))

print(min(1000, 900))

print(floor(345.98))

print(ceil(3.1))

name = input("Enter yor name: ")
print("Hello " + name + ". Welcome !!!")

num_1 = input("Input your first number: ")
num_2 = input("Input your second number: ")
product = float(num_1) * float(num_2)
print("The product of " + num_1 + " and " + num_2 + " is " + str(product))


#madlib
dog = input("Enter a dog breed ")
car = input("Enter a car model: ")
phone = input("Enter a phone brand: ")

print(dog + " are so violent and noisy.")
print("Louder than a " + car + ".")
print("And more expensive than a " + phone + " !")
"""
"""
#sumation calculator
def add(a, b):
    return a + b 

num_1 = input("Enter your first number: ")
num_2 = input("Enter your second number: ")
num_3 = input("Enter your third number: ")
num_4 = input("Enter your fourth number: ")
num_5 = input("Enter your fifth number: ")
num_6 = input("Enter your sixth number: ")

result_1 = add(float(num_1), float(num_2))
result_2 = add(float(num_3), float(num_4))
result_3 = add(float(num_5), float(num_6))

sum_list = [result_1, result_2, result_3]

print(sum_list)

#list functions
mood_history = ["sad", "excited", "angry"]

mood_history.append("happy")

print(mood_history)

for i in mood_history:
    print(i)

mood_history = []
mood_1 = input("How do you feel? ")
mood_2 = input("How do you feel? ")
mood_3 = input("How do you feel? ")
mood_4 = input("How do you feel? ")
mood_5 = input("How do you feel? ")

mood_history.append(mood_1)
mood_history.append(mood_2)
mood_history.append(mood_3)
mood_history.append(mood_4)
mood_history.append(mood_5)

print(mood_history)

#avg calculator
values = [
    float(input("Enter the first value: ")),
    float(input("Enter the second value: ")),
    float(input("Enter the third value: "))
]

average = (values[0] + values[1] + values[2]) / len(values)

print("The average of the values is: " + str(average))


#mood tracker using while loop
mood_history = []
mood = input("How do you feel today? ").lower()

while mood != "stop":
    mood_history.append(mood)
    
    if mood == "happy":
           print("Keep that smile on")
    elif mood == "sad":
             print("What's wrong, cheer up")
    elif mood == "angry":
             print("Take a deep breathe and calm down")
    else:
        print("Got it !")

    mood = input("How do you feel today? ").lower()



print("How you've felt today\n" + ", ".join(mood_history))


"""
"""
#mood tracker using while loop
mood_history = []
mood = input("How do you feel today? ").lower()

while True:
    if mood == "":
        mood = input("How do you feel today? ").lower()
        continue
    if mood == "stop":
        break
    if mood != "stop":
        mood_history.append(mood)

        if mood == "happy":
            print("Keep that smile on!")
        elif mood == "sad":
            print("What's wrong?")
        elif mood == "angry":
            print("Take a deep breathe and calm down")
        else:
            print("Got it")

        mood = input("How do you feel today? ").lower()

total_moods = len(mood_history)
first_mood = mood_history[0]
last_mood = mood_history[-1]

print("Total moods entered: " + str(total_moods))
print("moods: " + ", ".join(mood_history))
print("first mood: " + first_mood)
print("last mood: " + last_mood)



#mood tracker using for loop
mood_history = []

print("Welcome to EVOS...")

mood_sum = int(input("How many mood do you want to enter? "))

print("...OKAY...")

for mood in range(mood_sum):
    mood = input("How do you feel? ").lower().strip()

    if mood == "":
        print("You didn't enter anything, try again")
        continue

    mood_history.append(mood)

    if mood == "happy":
        print("Keep that smile on!")
    elif mood == "angry":
        print("Take a deep breathe and calm down")
    elif mood == "sad":
        print("Cheer up bro !")
    else:
        print("Got it !")

first_mood = mood_history[0]
last_mood = mood_history[-1]
total_moods = len(mood_history)


print("mood summary... Loading")
print("total moods: " + str(total_moods))
print("first mood: " + first_mood)
print("last mood: " + last_mood)
print("your moods: " + ", ".join(mood_history))
print("...")
"""

#Mood Tracker Premium version including for and while loops, and conditionals
mood_history_premium = []
mood_history_basic = []

print("Welcome to EVOS...")
print("You are on the premium version...")
print("...redirecting... Loading...")

print("You have ten free trials...")
for mood  in range(10):
    mood = input("How do you feel? ").lower().strip()

    if mood == "":
        print("You didn't enter anything, try again...")
        continue

    mood_history_premium.append(mood)

    if mood == "happy":
        print("Keep that smile on!")
    elif mood == "angry":
        print("Take a deep breathe and calm down")
    elif mood == "sad":
        print("Cheer up bro !")
    else:
        print("Got it !")

print("Your Trial is Up !")
print("redirecting to free mode... Loading...")

mood = input("How do you feel? ").lower().strip()
while True:
    if mood == "":
           mood = input("How do you feel today? ").lower().strip()
           continue

    if mood != "stop":
        mood_history_basic.append(mood)
        
        if mood == "happy":
            print("That's awesome")
        elif mood == "angry":
            print("Chill bro")
        elif mood == "sad":
            print("Everything will be fine !")
        else:
            print("Okay !")
    
        mood = input("How do you feel? ").lower().strip()


    if mood == "stop":
        break

total_moods = len(mood_history_premium) + len(mood_history_basic)
premium_moods = mood_history_premium
basic_moods = mood_history_basic

print("Mood Summary... LOADING...")
print("Total Moods: " + str(total_moods))
print("Premium Moods: " + ", ".join(premium_moods))
print("Basic Moods: " + ", ".join(basic_moods))
print("Powered by EVOS...")
