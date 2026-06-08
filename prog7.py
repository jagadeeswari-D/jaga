#Triangle Type Checker – Determine Equilateral, Isosceles, or Scalene.
a=float(input("Enter the first angle: "))
b=float(input("Enter the sec angle : "))
c=float(input("enter the third angle : "))
if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    if (a==b==c==60):
        print("This is equalateral triangle !")
    elif (a==b or b==c or a==c):
        print("this is Isosceles triangle !")
    else :
        print("this is scalen triangel !")
else:
    print("you have entered wrong input ! ")
