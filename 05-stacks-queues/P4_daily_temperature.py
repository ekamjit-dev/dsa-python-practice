temp =[73,74,75,71,69,72,76,73]
s =[]
ans = [0] * len(temp)

for i in range(len(temp)-1,-1,-1):
    current = temp[i]

    while s and temp[s[-1]] <= current:
        s.pop()

    if not s:
        ans[i] = 0
    else:
        ans[i] = s[-1] - i 

    s.append(i)       

print(ans)      
