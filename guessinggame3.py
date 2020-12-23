import random
highest= 100
answer= random.randint(1,highest)
#print(answer) #todo :Remove after testingu
guess=0
while guess != answer:
    guess=int(input("Plz Guess a No between 1 to 100 : \n"))
    if guess==answer:
        print("You got it correct first time")
        break
    elif guess<answer:
        print("Plz Guess higher")
        guess=int(input("\n"))
        if guess==answer:
            print('u got it right this time')
            break
        else:
            print("Try again")
    elif guess>answer:
        print("Plz Guess Lower")
        guess=int(input("Try Once more:\n"))
        if guess==answer:
            print("Bingo \n u r ryt!")
            break
        else:
            print("Try Again")
    else:
        print("Wrong")
        print(answer)