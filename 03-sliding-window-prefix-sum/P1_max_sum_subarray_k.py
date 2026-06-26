l = [2,1,5,1,3,2]
k = 3

window_sum = 0

for i in range(0,3):
    window_sum += l[i]

max_sum = window_sum    

for i in range(k , len(l)):
    window_sum = window_sum - l[i - k] + l[i]

    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)    