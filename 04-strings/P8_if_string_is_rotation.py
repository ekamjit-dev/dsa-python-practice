def if_string_rotation(s1,s2):

    if len(s1) != len(s2):
        return False
    
    double = s1+s1
    return s2 in double

print(if_string_rotation("abcd","cdab"))