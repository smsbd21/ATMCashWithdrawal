# nested if -- else control statement

mahin, mim, sazzad = 15, 22, 18

if mahin > mim:
    if mahin > sazzad:
        print("Mahin is elder than all")
    else:
        print("Sazzad is elder than all")
elif mim > sazzad:
    print("Mim is elder than all")
else:
    print("Sazzad is elder than all")