#Electricity Bill Calculator – Calculate bill based on slab rates.
u=int(input("Enter the number of electricity units consumed:"))
if u<=100:
    bill=u*0.5
elif u<=200:
    bill=100*0.5+(u-100)*0.75
elif u<=300:
    bill=100*0.5+100*0.75+(u-200)*1.20
else:
    bill=100*0.5+100*0.75+100*1.20+(u-300)*1.50
print("Your electricity bill is: Rs.",bill)
