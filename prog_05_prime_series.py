def return_primes(n):
    my_list = []

    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            my_list.append(i)

    return my_list

num = int(input("Enter your number : "))
print(return_primes(num))
