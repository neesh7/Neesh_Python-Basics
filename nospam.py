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
#Approach 1
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    # print(meal)  #This is'nt that effective cz this causes our output to be printed on seprate lines.
    print(meal, end=", ")
print("*"*80)
#Approach 2
for meal in menu:
    for item in menu:
        if item !="spam":
            print(item)
    