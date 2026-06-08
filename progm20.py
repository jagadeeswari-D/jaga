#Smart Traffic Signal System – Set green signal duration based on vehicle count
vc=int(input("Enter the number of vehicles waiting at the traffic signal:"))
if vc<10:
    print("Green signal duration is 30 seconds.")
elif vc>=10 and vc<20:
    print("Green signal duration is 45 seconds.")
else:
    print("Green signal duration is 60 seconds.")
