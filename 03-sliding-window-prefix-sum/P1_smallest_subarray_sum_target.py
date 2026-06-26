l = [2,3,1,2,4,3]
target = 7

left = 0
right = 0
window_sum = 0
min_length = float('inf')

for right in range(len(l)):
    window_sum += l[right]

    while window_sum >= target:
        min_length = min(min_length , right - left + 1)
        window_sum -= l[left]
        left +=1

print(min_length)        
