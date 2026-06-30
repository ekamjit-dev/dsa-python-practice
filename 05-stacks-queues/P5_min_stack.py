l = [45,87,1,92,8,76]
s =[]
min_s = []

for i in range(len(l)):
    x = l[i]

    s.append(x)

    if len(min_s) == 0 or x < min_s[-1]:
        min_s.append(x)
    else:
        min_s.append(min_s[-1])

# testing pop behavior 

s.pop()
min_s.pop()
s.pop()
min_s.pop()
s.pop()
min_s.pop()
s.pop()
min_s.pop()

print("Stack:", s)
print("Min Stack:", min_s)
  