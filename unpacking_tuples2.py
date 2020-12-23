welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
# # Indexing works similar in list , tuple or a string .it uses square brackets
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# instead of using indexing in order to print the title , artist and year of album we can use unpacking of tuples in order to do that.
# Let's unpack the tuples for this scenario
title, artist, year = metallica
print(title)
print(artist)
print(year)
print("*"*80)
table = ("coffee Table",200,100,15,1200)
#area of table
print(table[1]*table[2])
print("_"*80)
# it's very likely to do mistakes with indexing while dealing with tuples so we would use unpacking of tuples in order to calculate area of table
name, length, breadth, height, price = table
print(length*breadth)
print(price, "Rupees")
print()