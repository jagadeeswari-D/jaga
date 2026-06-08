 #Discount Calculator – Apply discount based on purchase amount
a=float(input("Enter the purchase amount: "))
if a >= 1000:
    discount = a * 0.1
    print("You get a 10% discount of:", discount)
    a-= discount
    print("Purchase amount after discount:", a)
elif a >= 500:
    discount = a * 0.05
    print("You get a 5% discount of:", discount)
    a-= discount
    print("Purchase amount after discount:", a)
else:
    discount = 0
    print("No discount applicable.")

