# task 1
x = 1
while True:
    print(x,end=" ")
    if x % 3 == 0:
        print("")
    if x == 9:
        break
    x += 1

# task 2.a
for x in range(4):
    for y in range(4):
        print("*",end=" ")
    print("")

# task 2.b
for x in range(4):
    for y in range(x+1):
        print("*",end=" ")
    print("")

# task 2.c
for x in range(1,5):
    for y in range(x):
        print(x,end=" ")
    print("")

# task 2.d
for x in range(4):
    num = 1
    for y in range(x+1):
        print(num,end=" ")
        num += 2
    print("")
