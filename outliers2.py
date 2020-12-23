data = [5, 6,102,109,178,188,189,191,194,199,350,356]  # total no of element in list =12
print((data))
min_valid = 100
max_valid = 200
stop = 0
#this code will work only the data is sorted
#to process the low values in the list
for index,value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)   #for debugging
del data[:stop]
print("NOw the intial Two entries have been deleted which was <100")
print(data) # total no of element in list =10
print("*"*80)
start= 0
for index in range(len(data)-1,-1,-1):
    #print(index) # total no of element in list =10 so indexing is 0,1,2,3,..,9
    if data[index] <= max_valid:
        start= index
        break
print(start) #for debbuging
del data[start:]
print(data) # total no of element in list =8 as we deleted no's >200