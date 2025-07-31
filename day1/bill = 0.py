bill = 0
total = 0
bill = (int)(input("enter your bill amount "))
print("what % whould you like to tip")
per = (int)(input("1 for 10% , 2 for 20% , 3 for 30%  "))
if(per == 1):
    total = bill+(bill* 0.1)
    print(total)
elif(per == 2):
    total = bill+(bill* 0.2)
    print(total)
elif(per == 3):
    total = bill+(bill* 0.3)
    print(total)
else:
    print("invalid value")
