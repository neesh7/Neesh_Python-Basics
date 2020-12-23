shopping_list = ["milk", "jam", "pasta", 'spam', "grocery"]
print("Our Shopping List is :")
for item in shopping_list:
    print("Buy  " + item)
# when we go to shopping ofcourse buying spam makes no sense so we would exclude this by writing
print("__________________________________________________________")
for item in shopping_list:
    if item != "spam":
        print("Buy " + item)
print("_*-_" * 5)
# other way to do this is using continue and break in loops let's see how it's done
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)
# using break in a statement

print("-" * 80)
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)
print("The length of our Shopping list is = ",  shopping_list.__len__() )
