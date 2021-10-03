s, b = 0, 12365436
while b > 0:
    a = b % 10
    s = s + a
    b = b // 10

print("The value of s:", s)
