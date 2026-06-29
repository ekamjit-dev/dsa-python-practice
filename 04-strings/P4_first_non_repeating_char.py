def first_non_repeating(s):

    freq = {}

    for ch in s:
        if ch not in freq:
            freq[ch] = 1

        else:   
            freq[ch] +=1

    for ch in freq:
        if freq[ch] == 1:
            return ch

    return None

print(first_non_repeating("swiss"))                