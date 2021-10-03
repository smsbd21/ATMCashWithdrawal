w = input("Enter Value (C/F): ")
if w.upper() == "C":
    c = int(input("Enter Celsius Value: "))
    f = round(1.8 * c + 32, 2)
    print("Fahrenheit Value is:", f)
else:
    f = int(input("Enter Fahrenheit Value: "))
    c = round((f - 32) / 1.8, 2)
    print("Celsius Value is:", c)