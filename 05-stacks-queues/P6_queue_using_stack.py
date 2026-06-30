l = [1,2,3,4,5]
s1 =[]
s2 =[]

for i in range(len(l)):
    x = l[i]

    s1.append(x) 
  
if not s2:
     while s1:
        s2.append(s1.pop())

print(s2.pop())

if not s2:
     while s1:
        s2.append(s1.pop())

print(s2.pop())