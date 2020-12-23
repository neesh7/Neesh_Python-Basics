#todo: extract capital letters from the string

# quote= " Beauty lies in the Eye of Beholder "
# for caps in quote:
#     if caps.isupper():
#         print(caps)
# for char in quote:
#     if char.isupper():
#         print(char)

import random
ans=random.randint(1,100)
guess=0
print(ans)
print("Enter a No between 1 to 100")
guess=int(input())
while guess !=ans:
    guess=int(input())
    if guess==ans:  
        print("u r ryt")
        break
    elif guess<ans:
        print("guess higher")
        continue
    elif guess>ans:
        print("Guess Lower")
        continue