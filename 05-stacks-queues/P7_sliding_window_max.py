from collections import deque

num = [1,3,-1,-3,5,3,6,7]
k = 3
dq = deque()
ans = []

for i in range(len(num)):
    current = num[i]

    if dq and dq[0] <= i - k:
        dq.popleft()

    while dq and num[dq[-1]] <= current:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        ans.append(num[dq[0]])   

print(ans)         




    

