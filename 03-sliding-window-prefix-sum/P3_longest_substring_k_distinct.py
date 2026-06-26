s = "eceba"
k = 2

freq = {}
left = 0
max_length = 0

for right in range(len(s)):
    ch = s[right]
    
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] =  freq[ch] + 1
    
    while len(freq) > k:
        freq[s[left]] -=1

        if freq[s[left]] == 0:
            del freq[s[left]] 

        left +=1

    current_length = right - left + 1
    max_length = max(max_length , current_length)

print(max_length)             
