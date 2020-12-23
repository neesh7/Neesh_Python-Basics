low=1
high=1000
print(" Plz Think of a Number between {} and {} ".format(low,high))
input("Press Enter to Start")
guesses=1
H="H" #we r declaring h,c,l for using casfold later in the problem cz casefold normally can be used with variables
L="L"
C="C"
while low != high:
    #print("\t Guessing in the range of {} to {}".format(low,high))
    guess= low+(high-low)//2
    high_low=input(" Let Me guess , My guess is {} \n So tell Me was i correct Enter 'C' if i was correct\tIf Not then Tell me !"
                   "Should I Guess Higher or Lower\t Enter 'H' for Higher or 'L' for Lower  ".format(guess))
    if high_low==H.casefold():
        low= guess +1
    elif high_low==L.casefold():
        high=guess-1
    elif high_low==C.casefold():
        print("I got it correct in {} Guess ".format(guesses))
        break
    else :
        print("Plz Enter H,L or C")

    #guesses= guesses+1 #this line help us to count the no. of guesses it takes computer to find our real answer
    guesses+=1 # this is called Augmented Assignment

else:
    print( " I thought of the Number {}".format(H))
    print("i got it in {} Guesses".format(guesses))
