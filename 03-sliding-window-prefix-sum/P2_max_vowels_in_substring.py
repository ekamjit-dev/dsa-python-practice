s = "abciiidef"
k = 3

count = 0

for i in range(0,3):
    if s[i] in "aeiou":
        count +=1

max_count = count     

for i in range(k , len(s)):
    if s[i - k] in "aeiou":
        count -=1

    if s[i] in "aeiou":
        count +=1

    if count > max_count:
        max_count = count       

print(max_count)        