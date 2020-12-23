albums_lists = ["Welcome to my Nightmare", "Alice Cooper", 1975,
                "Bad Company", "Bad Company", 1974,
                "Nightflight", "Budgie", 1981,
                "More Mayhem", "Emilda May", 2011,
                "Ride the Lightning", "Metallica", 1984,
                ]
print(len(albums_lists))  # This is a list containing 15 items in it
print("_" * 80)
albums_list_tup = [("Welcome to my Nightmare", "Alice Cooper", 1975),
                   ("Bad Company", "Bad Company", 1974),
                   ("Nightflight", "Budgie", 1981),
                   ("More Mayhem", "Emilda May", 2011),
                   ("Ride the Lightning", "Metallica", 1984,
                    )]
print(len(albums_list_tup))  # # albums_list-tup is a list containing 5 tuples
for name, artist, year in albums_list_tup:  # unpacking tuples in a single line during for loop
    print("Album: {} , Artist: {} , Year: {} ".format(name, artist, year))
# Or we can use this Approach
print()
for albums in albums_list_tup:  #unpacking tuples inside a loop
    name, artist, year = albums
    print("Album: {} , Artist: {} , Year: {} ".format(name, artist, year))