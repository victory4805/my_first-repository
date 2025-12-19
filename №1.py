n = int(input("Введите число: "))
i = 1
while i <= n:
    print(i)
    i += 1

n = int(input("Введите число: "))
sum = 0
for i in range(1, n+1):
    sum = i + sum
print(sum)
    