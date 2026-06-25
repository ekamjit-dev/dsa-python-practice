word = "teeter"

count_dict = {}

for letter in word:
    if letter in count_dict:
        count_dict[letter] +=1

    else:
        count_dict[letter] = 1

for letter in word:
    if count_dict[letter ]== 1:
        print(letter)    
        break    

print(count_dict)
        
