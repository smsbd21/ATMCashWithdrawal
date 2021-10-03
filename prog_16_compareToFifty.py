def compareToFifty(value1,value2):
    if type(value1) == int and type(value2) == int and value1 > 0 and value2 > 0:
        valuetotal = value1 + value2
        if valuetotal < 50:
            return "Below 50"
        if valuetotal > 50:
            return "Above 50"
        if valuetotal == 50:
            return "Equal to 50"
    if type(value1) or type(value2) == str:
        if type(value1) == str and type(value2) == int:
            if value1.isdigit():
                value1 = int(str(value1))
                valuetotal = value1 + value2
                if valuetotal < 50:
                    return "Below 50"
                if valuetotal > 50:
                    return "Above 50"
                if valuetotal == 50:
                    return "Equal to 50"
            elif value1.isalpha():
                return "Invalid Input"
        if type(value2) == str and type(value1) ==int:
                    if value2.isdigit():
                        value2 = int(str(value2))
                        valuetotal = value1 + value2
                        if valuetotal < 50:
                            return "Below 50"
                        if valuetotal > 50:
                            return "Above 50"
                        if valuetotal == 50:
                            return "Equal to 50"
                    elif value2.isalpha():
                        return "Invalid Input"
        if type(value1) == str and type(value2) == str:
            if value2.isdigit() and value1.isdigit():
                value1 = int(str(value1))
                value2 = int(str(value2))
                valuetotal = value1 + value2
                if valuetotal < 50:
                    return "Below 50"
                if valuetotal > 50:
                    return "Above 50"
                if valuetotal == 50:
                    return "Equal to 50"
            elif value1.isalpha() or value2.isalpha():
                return "Invalid Input"
    if type(value1) or type(value2) == float:
        return "Invalid Input"
    if type(value1) or type(value2) == bool:
        return "Invalid Input"       

val1=input("Enter first value:")
val2=input("Enter second value:")
print(compareToFifty(val1,val2))
  