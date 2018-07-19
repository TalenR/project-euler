import math
# returns the 10001st prime

nfacs = []

def primeFactors(n):
    while n % 2 == 0:
        nfacs.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            nfacs.append(i)
            n = n / i
    if n > 2:
        nfacs.append(n)

count = 1
m=3
while count < 10001:
    primeFactors(m)
    if len(nfacs) == 1:
        count += 1
    m += 2
    nfacs = []

print(m-2)
