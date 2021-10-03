#n_1=int(input("Input height of tree between 1-19:"))
def digital_conifer(n_1):
 k=0
 k2=0
 while k < n_1:
 	block= 2*k2

 asterk= 1 + block
 whitespace =(19)-k
 print((" " * whitespace) + "*"* asterk )
 k=k+1
 k2=k2+1
 
 if n_1>16:
  print(" " * 18 + "*" *3)
  print(" " * 18 + "*" *3)
  print(" " * 18 + "*" *3)
 elif n_1 > 8:
  print(" " * 18 + "*" *3)
  print(" " * 18 + "*" *3)
  print(" " * 18 + "*" *3)
 else:
  print(" " * 19 + "*" *1)
  print(" " * 19 + "*" *1)
 
 print("*" *38)

digital_conifer(19)