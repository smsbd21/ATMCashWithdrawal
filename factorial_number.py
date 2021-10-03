num = int(input("Enter Number: "))
fact, f, n = 1, 1, 2

for i in range(2, num + 1):
    fact *= i

print("Factorial value of n using for loop:", fact)

while n <= num:
    f *= n
    n += 1
print("Factorial value of n using while loop:", f)

