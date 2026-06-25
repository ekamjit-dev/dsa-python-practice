word_A = "listen"
word_B = "silent"

count_dict1 = {}
count_dict2 = {}

if len(word_A) != len(word_B):
    print("Not Anagram")
else:
    for letter in word_A:
        if letter in count_dict1:
            count_dict1[letter] +=1

        else:
            count_dict1[letter] = 1
            

    for letter in word_B:
        if letter in count_dict2:
            count_dict2[letter] +=1

        else:
            count_dict2[letter] = 1


    if count_dict1 == count_dict2:
        print("Anagram")
    else:
        print("Not Anagram")


