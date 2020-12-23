panagram_one = "The Quick brown Fox Jumps over the lazy dog"
panagram_two = """The Quick brown 
Fox Jumps
 \tover\t the lazy dog"""

words1 = panagram_one.split()
print(words1)
words2 = panagram_two.split()
print(words2)

numbers= "992,22,14,24,553,2324"
print(numbers)
print(numbers.split(","))
# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.
