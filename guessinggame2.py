import random
highest = 10
answer = random.randint(1,highest)
#print(answer) #todo :Remove after testing
guess=int(input("Plz Guess a No between 1 to 10 : \n"))
if guess==answer:
    print("You got it correct first time")
elif guess<answer:
    print("Plz Guess higher")
    guess=int(input("That's your last chance:\n"))
    if guess==answer:
        print('u got it right this time')
    else:
        print("better luck next time")
        print("The answer was {}".format(answer))
elif guess>answer:
    print("Plz Guess Lower")
    guess=int(input("That's your last chance:\n"))
    if guess==answer:
        print("Bingo \n u r ryt!")
    else:
        print("Better luck Net time")
        print("The answer was {}".format(answer))
else:
    print("Wrong")
    print(answer)