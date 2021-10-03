# mes="smssumon"
def char_rep(mes):
    rChar = ""
    flag = False
    for i in range(len(mes) - 1):
        if flag:
            flag = False
        elif mes[i] == mes[i + 1]:
            rChar += mes[i]
            rChar += "*"
            flag = True
        else:
            rChar += mes[i]
    rChar += mes[-1]
    return rChar


# ctxt=input("Enter your char:")
print(char_rep("abcabc"))
