#ATM Withdrawal System – Validate balance, withdrawal amount, and minimum balance.
cb=50000.0
mb=500.0
print("welcome ")
print("your current ammount is ",cb)
wa=float(input("enter the amount u want to withdraw : "))
if wa<=0:
    print(" Invalid ! enter valid amount you want to withdraw :")

elif(wa > cb):
    print(""" tranction failed :
          your doesent have sufficent ammount to withdraw""")
elif (cb-wa)<mb:
    print("""please ! maintain sufficiant ammount
             Transcation faiel""")
else:
    print("your transction succesfully")
    cb=cb-wa
    print("your remaining blance is : ",cb)