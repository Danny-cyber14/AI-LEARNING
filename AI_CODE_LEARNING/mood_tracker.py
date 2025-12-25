import random

#Mood Tracker Premium version including for and while loops, and conditionals
mood_history_premium = []
mood_history_basic = []
mood_dict = {}

print("Welcome to EVOS...")
print("You are on the premium version...")
print("...redirecting... Loading...")

print("You have ten free trials...")
for mood  in range(10):
    mood = input("How do you feel? ").lower().strip()

    if mood == "":
        mood = input("How do you feel? ").lower()
        mood_history_premium.append(mood)
        continue

    happyResponses = [
    "That's awesome to hear! Keep that energy going ",
    "Love that for you! What's making you feel so good?",
    "Nice! Sounds like today is treating you well.",
    "That’s great — enjoy every moment of it!",
    "Your good mood is contagious ",
    "Glad you're feeling happy today!"
    ]

    angryResponses = [
    "That sounds really frustrating. Want to talk about it?",
    "I get why you'd feel angry — that’s tough.",
    "Take a deep breath, I'm here with you.",
    "It’s okay to feel mad sometimes.",
    "Let’s slow things down and figure this out together.",
    "That situation sounds really irritating."
    ]

    sadResponses = [
    "I'm really sorry you're feeling this way.",
    "That sounds heavy — you don’t have to go through it alone.",
    "I’m here for you, even if you just want to vent.",
    "It’s okay to feel sad sometimes.",
    "Want to tell me what’s been weighing on you?",
    "You matter, and your feelings are valid."
    ]
    
    happy_choice = random.choice(happyResponses)
    sad_choice = random.choice(sadResponses)
    angry_choice = random.choice(angryResponses)

    if mood == "happy":
        print(happy_choice)
    elif mood == "angry":
        print(angry_choice)
    elif mood == "sad":
        print(sad_choice)
    else:
        print("Got it !")

    mood_history_premium.append(mood)


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

for moods in mood_history_basic:
    if moods in mood_dict:
        mood_dict[moods] += 1
    else:
        mood_dict[moods] = 1

for moods in mood_history_premium:
    if moods in mood_dict:
        mood_dict[moods] += 1
    else:
        mood_dict[moods] = 1

print("Mood Summary... LOADING...")
print(f"Total Moods: {str(total_moods)}")
print("Premium Moods: " + ", ".join(premium_moods))
print("Basic Moods: " + ", ".join(basic_moods))

for moods in mood_dict:
    print(moods + ":", str(mood_dict[moods]))

common_mood = max(mood_dict, key=mood_dict.get)
print(f"most common mood: {common_mood}")

if common_mood == "happy":
    print("You've been happy lately, keep that smile up!")
elif common_mood == "angry":
    print("You've been angry lately, turn that frown upside down")
elif common_mood == "sad":
    print("You've been sad lately, cheer up!")
else:
    print(f"You've been {common_mood} lately, interisting! How about we talk about this")

print("Powered by EVOS...")