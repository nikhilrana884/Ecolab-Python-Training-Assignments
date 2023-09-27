l = int(input("Enter the min value of range:"))
r = int(input("Enter the max value of range:"))

for i in range(l, r+1):
    flag = 0

    if i<2:
        continue

    if i==2:
        print(i, sep=" ")
        continue

    for x in range(2, i):
        if i%x == 0:
            flag = 1
            break

    if flag == 0:
        print(i, sep=" ")
        