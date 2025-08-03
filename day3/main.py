from c_to_f import CtoF, FtoC

n = int(input("Press 1 to convert from °C to °F, or press 2 to convert from °F to °C: "))

if n == 1:
    num = float(input("Enter the temperature in °C: "))
    f = CtoF(num)
    print(f"{num}°C is {f:.2f}°F")
elif n == 2:
    num = float(input("Enter the temperature in °F: "))
    c = FtoC(num)
    print(f"{num}°F is {c:.2f}°C")
else:
    print("Invalid selection.")
