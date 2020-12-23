for index, character in enumerate("abcdefgh"):  # index will get the indexes of the character and character will get the values.
    print(index, character)
#enumerate in Tuples
for t in enumerate("abcdefgh"):
    # print(t)
    # print("#"*80)
    index, character = t        # Line 7 is just a shorthand for line 5 both of them does the same things
    print(index,character)
print("-"*80)
index, character = 0, "a"
print(index)
print(character)

