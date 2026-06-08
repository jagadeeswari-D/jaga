#Grade Classification – Display grade based on marks.
a=int(input("enter your mark : "))
if a>=90 and a<=100:
    print("your grade is A")
    print("Your are outstanding")
elif a>=80 and a<=89  :
    print("your grade is B")
    print("Very good")
elif a>=70 and a<=79:
    print("your grade is C")
    print("Good")
elif a>=60 and a<=69:
    print("Your grade is D")
    print("statisfied")
elif a>=50 and a<=59:
    print("your grade is E")
    print("you need improvement")
elif a>=40 and a<=49:
    print("you are fail")
else:
    print("invalid input")


