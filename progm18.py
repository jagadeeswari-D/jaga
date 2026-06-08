#Movie Ticket Pricing – Calculate ticket price using multiple conditions
a=int(input("Enter your age:"))
d=input("Enter the day of the week:")
if a<12:
    print("Your ticket price is rupees 5.")
elif a>=12 and a<60:
    if d.lower() in ["monday", "tuesday", "wednesday", "thursday"]:
        print("Your ticket price is rupees 10.")
    else:
        print("Your ticket price is rupees 15.")
else:
    print("Your ticket price is rupees 8.") 
