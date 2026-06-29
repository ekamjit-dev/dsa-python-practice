def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {} 

    for ch in s1:
        if ch not in freq1:
            freq1[ch] = 1
        else:
            freq1[ch] +=1    

    for ch in s2:
        if ch not in freq2:
            freq2[ch] = 1
        else:
            freq2[ch] +=1    
        
    return freq1 == freq2

print(is_anagram("silent","listen"))