parrot = 'Norwegian Blue'
print(" Let's Check ! You enter a Letter i'll Check it is available in Norwegian Blue or Not "
      "Quiet Basic yes  !! \n ok let's play")
letter = input("type a character ?")
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
    print("{} is available in Norwegian Blue At Index postion {}".format(letter,"Upss!! This is work in progress"))
else:
    print("not available ")
