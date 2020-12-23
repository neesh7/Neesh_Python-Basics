answer = 7
print("How many Wonders are there in world")
guess = int(input())
# Simple Code #
# if guess<answer:
#     print("Please Guess Higher ")
# elif guess>answer:
#     print("Please Guess lower")
# else:
#     print("you are Right and Those Wonders Are \n Taj Mahal \n The Great Pyramid of Giza\n "
#           "The Colossus of Rhodes\n The Lighthouse of Alexandria\n The Mausoleum\n "
#           "The Temple of Artemis \n The Statue of Zeus")
# More Responsive code(Adding Second Guess) #
# if guess<answer:
#     print("Please Guess Higher ")
#     guess=int(input())
#     if guess==answer:
#         print(("Well done"))
#         print("you are Right and Those Wonders Are \n Taj Mahal \n The Great Pyramid of Giza\n "
#               "The Colossus of Rhodes\n The Lighthouse of Alexandria\n The Mausoleum\n "
#               "The Temple of Artemis \n The Statue of Zeus")
#     else:
#         print("Better Luck next Time")
# elif guess>answer:
#     print("Please Guess lower")
#     guess=int(input())
#     if guess==answer:
#      print("Bravo")
#      print("you are Right and Those Wonders Are \n Taj Mahal \n The Great Pyramid of Giza\n "
#            "The Colossus of Rhodes\n The Lighthouse of Alexandria\n The Mausoleum\n "
#            "The Temple of Artemis \n The Statue of Zeus")
#     else:
#         print("Better Luck next time")
# else:
#     print("you are Right and Those Wonders Are \n Taj Mahal \n The Great Pyramid of Giza\n "
#           "The Colossus of Rhodes\n The Lighthouse of Alexandria\n The Mausoleum\n "
#           "The Temple of Artemis \n The Statue of Zeus")


if guess != answer:  # use of not Equals to concept And Nested If else Concept
    if guess < answer:
        print("Plz Guess Higher")
    else:
        print("Plz Guess Lower")
    guess = int(input())
    if guess == answer:
        print("You got it right this time")
    else:
        print("Again wrong")
else:
    print("You Got it right for the first time")
