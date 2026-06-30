l = [1,7,66,98,34]
stack =[]
ans = [0] * len(l)

for i in range(len(l)-1 , -1, -1):
    current = l[i]
 
    while stack and stack[-1] <= current:
        stack.pop()

    if not stack:
        ans[i] = -1
    else:
        ans[i] = stack[-1]

    stack.append(current)        

print(ans)        
