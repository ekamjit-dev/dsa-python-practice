def two_sum(l , target):
    l.sort()
    left = 0
    right = len(l) - 1

    while left < right:
        current_sum = l[left] + l[right]
        if current_sum == target:
            return l[left] , l[right]
        elif current_sum < target:
            left +=1
        else:
             right -=1

    return None

l= []

print("Enter The Size Of The List:")
n = int(input())

if n==0:
    print("List Is Empty")
elif n<0:
    print("Invalid Number, Not Allowed")
else:
    print(f"Enter {n} Elements")
    for i in range(n):
        num = int(input(f"Enter List Element {i+1}: "))
        l.append(num)

    print(f"List: {l}")
    print("Enter The Target: ")
    target = int(input())

    result = two_sum(l, target)

    if result:
        print(f"Target Found: {result[0]} + {result[1]} = {target}")
    else:
        print("No Target Found")

        

