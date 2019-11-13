#Problem 1
#sum of all multiples of 3 or 5 belowe 1000

sum = 0
for a in range(1,1000):
    if (a%3) == 0 or (a%5) == 0:
        sum += a
print("Sum - ",sum)