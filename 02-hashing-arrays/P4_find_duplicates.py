l = [1,5,5,1,3,5,46,7]

count_dict = {}

for numbers in l:
    if numbers in count_dict:
        count_dict[numbers] +=1

    else:
        count_dict[numbers] = 1

print(count_dict)            

for key , value in count_dict.items():
    if value > 1:
        print(key)

