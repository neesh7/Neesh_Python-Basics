menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
#use alt+shift+up/down to navigate ur list up and down
#to count the no. of spam we are going to use spam function moreover .
for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal: #nested lists in a loop it will print the items of the list which is not containing the spam
            print(item)
    else:
        print("{} has a Spam Score of {} "
              .format(meal,meal.count("spam")))