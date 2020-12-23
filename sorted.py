pangram = "The quick brown fox jumps over the lazy dog" # a pangram is a english sentence which contains all alphabets
letters=sorted(pangram)  #here we give a string to sorted function but it returns a list
print(letters)
numbers=[1.2,4.5,0.9,1.34,9.9,4.7] #here we provide a list to sorted function and in return sorted function provides  list . so irrespective of input sorted function provides list as output
sorted_numbers= sorted(numbers)
print(sorted_numbers)
print(numbers)
numbers.sort()
print(numbers)
# #sort function modifies the original list
# another_sorted_numbers = numbers.sort()
# print(numbers)
# print(another_sorted_numbers)   #it will give output as note so assigning variable to a sort method is not a good idea
missing_letter = sorted("The quick brown lazy fox jumped over the lazy dog",key = str.casefold)
print(missing_letter)
print()
names = ["aditya,"
         "revathi",
         "Yatarth",
         "Zook"]
names.sort()
print(names)   #when we see the ouput we realise names are'nt sorted in order to sort them out we will use keyword argument
names.sort(key=str.casefold)
print(names)#so this time we get our names sorted in correct order without worrrying about caases


