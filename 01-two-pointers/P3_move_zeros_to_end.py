l = []

print("Enter The Size of The list: ")
n = int(input())

if n == 0:
    print("Empty List")
elif n<1:
    print("Invalid Digit")
else:
    print(f"Enter {n} Elements:")    
    for i in range(n):
        num = int(input(f"Enter Element {i+1}: "))   
        l.append(num)

    slow = 0
    fast = 0

    while fast < len(l):
        if l[fast] != 0:
            l[slow] = l[fast]
            slow +=1
        fast +=1
    while slow < len(l):
        l[slow] = 0
        slow += 1

    print(f"List: {l}")        


