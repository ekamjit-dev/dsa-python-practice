l = []

print("Enter The Size Of The List: ")
n = int(input())

if n == 0:
    print("List Is Empty")
elif n < 1:
    print("Invalid Digit")
else:
    print(f"Enter {n} Elements:")
    for i in range(n):
        num = int(input(f"Enter Elemment {i+1} Of The List: "))
        l.append(num)

    l.sort()

    slow = 0
    fast = 1

    while fast < len(l):
        if l[slow] == l[fast]:
            fast +=1
        else:
            slow +=1
            l[slow] = l[fast]
            fast +=1
    l = l[:slow+1]

    print("Result:", l)

                
                     
