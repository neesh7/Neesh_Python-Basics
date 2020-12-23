data = [5, 6,102,109,178,198,187,199,174,201,220,350,356]
#index  0, 1, 2,  3,  4,  5,  6,  7,  8,  9 ,10 ,11 ,12
print(data)
#suppose if we want manually to delete some data
del data[0:2]  # 5 and 6 will be removed
print(data)
del data[9:]
print(data)
print("#__________________________________________________")
data.sort()
print(data)
# #the above all technique is technique to delete a data manually
# min_valid = 100
# max_valid = 200
# for index , value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)
