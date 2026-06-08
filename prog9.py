#Voting Eligibility Checker – Check eligibility using age and citizenship.
a=int(input("Enter your age:"))
b=input("Enter your Nationality:")
if a>=18 and b.lower()=="india":
    print("You are elegible for voting")
else:
    print("you are not eligible for voting")
    

