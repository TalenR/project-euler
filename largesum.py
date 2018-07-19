import os
import math

#returns the first 10 digits of fifty hundred-digit numbers. Not working

os.chdir(r'C:\Users\pr5628de\Documents')

nums = []
with open('fiftynumbers.txt','r') as numbers:
    read_data = list(numbers.read())

for i in read_data:
    if i == '\n':
        continue
    nums.append(int(i))

print(read_data)
print(nums)

numbers = []
for i in range(0,100):
    numbers.append(nums[i*50:i*50+50])
print(numbers)

sums = []
for i in range (0,49):
    sums.append(sum(numbers[j][i] for j in range(0,99)))
print(sums)

print(sum(sums[i]*10**(49-i) for i in range(0,49)))

for i in range(1,12):
    sums[0] = sums[0]*10 +sums[i]

print(sums[0])

fullnums =[]
for j in range(0,99):
    fullnums[j] = sum(numbers[j][i]*10**(49-i) for i in range(0,49))

print(fullnums)
