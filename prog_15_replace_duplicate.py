def rep_duplicates(astr: str, mask="*"):
    from typing import Counter
    astr = astr.casefold()
    x = Counter[astr]
    for i in range(len(astr)):
        if x[astr[i]] > 1:
            if i == 0:
                astr = astr[0] + astr[1:].replace(astr[0], mask)
            else:
                astr = astr[:i + 1] + astr[i + 1:].replace(astr[i], mask)
    print("Result is:", astr)
    #return astr


#rword = "abbcaa"
#print(rep_duplicates(rword, "*"))
# gives ab*c**
rword = input("Enter your text here:")
rep_duplicates(rword, "*")
