import math

# returns the number under 1000000 with the longest collatz sequence

biggest = 0
high = 0

for i in range(1,1000001):
    n = i
    j = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3 + 1
        j += 1
    if j > high:
        biggest = i
        high = j

print(biggest)
