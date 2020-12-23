data = [104,101,4,105,308,103,5,107,100,306,106,102,108]
#this code works for sorted and unsorted both kind of listv
min_valid = 100
max_valid = 200
top_index = len(data)-1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(data, top_index-index)
        del data[top_index-index]


print(data)