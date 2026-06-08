#Simple Calculator – Perform +, -, *, / using conditional statements.
c=input("enter what opration do you want to use + - * / %  ")
a=float(input("enter first number : "))
b=float(input("enter sec number : "))
if c== "+":
    print(a,"+",b,"=",a+b)
elif c=="-":
    print(a,"-",b,"=",a-b)
elif c=="*" :
    print(a,"*",b,"=",a*b)
elif c=="/":
    if b==0:
        print("you can't divid by zero")
    else:
        print(a,"/",b,"=",a/b)
elif c=="%":
    print(a,"%",b,"=",a%b)
else :
    print("invalid input")

