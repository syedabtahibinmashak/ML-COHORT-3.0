#task 01
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))
if x>y and x>z :
    print("x is largest")
elif y>z and y>x :
    print("y is largest")
else :
    print("z is largest")

#task 02
f1 = float(input("Enter the CGPA of friend 1: "))
f2 = float(input("Enter the CGPA of friend 2: "))
f3 = float(input("Enter the CGPA of friend 3: "))
if f1<f2 and f1<f3 :
    print("Friend 1 has the lowest CGPA")
elif f2<f1 and f2<f3 :
    print("Friend 2 has the lowest CGPA")
else :
    print("Friend 3 has the lowest CGPA")
avg = (f1+f2+f3)/3
print(f"Average CGPA: {avg}")
