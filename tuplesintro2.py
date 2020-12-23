welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
# Indexing works similar in list , tuple or a string .it uses square brackets
print(metallica[0])
print(metallica[1])
print(metallica[2])
# tuples are immutable so we can't assign new values to an Tuple
# metallica[0] = "THis is a Great day"  # tuple don't support item assignmetn
metallica2= list(metallica)  #converting a tuple into a list
print(metallica2)
metallica2[0] = "Master puppets"
print(metallica2)

