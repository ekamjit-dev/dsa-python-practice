prices = [100,65,34,2,89]
s = []
ans = [0] * len(prices)

for i in range(len(prices)):
    current = prices[i]

    while s and prices[s[-1]] <= current:
        s.pop()

    if not s:
        ans[i] = i + 1
    else:
        ans[i] = i - s[-1]

    s.append(i)

print(ans)                
