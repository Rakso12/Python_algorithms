sum_1 = 0
sum_2 = 0
diff = 0
for liczba in range(1,101):
    sum_1 += pow(liczba,2)

for liczba in range(1,101):
    sum_2 += liczba
sum_2 = pow(sum_2,2)

diff = sum_2 - sum_1
print(diff)