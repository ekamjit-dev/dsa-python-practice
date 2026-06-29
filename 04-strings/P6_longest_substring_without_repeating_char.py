def longest_substring_without_repeating_char(s):

    left = 0
    char = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in char:
            char.remove(s[left])
            left +=1

    char.add(s[right])

    current_length = right - left + 1
    max_length = max(current_length, max_length)        

    return max_length

print(longest_substring_without_repeating_char("abcabcbb"))
