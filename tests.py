import math

count = 0
total = 0
n = 3
m = 5
tao = 1.262

while count <= n:
    total += n ** count / math.factorial(count) * tao ** count
    count += 1
factorial = math.factorial(n)
test_ = n ** n / factorial * tao ** n + 1 * (1 - tao ** m) / 1 - tao
p_0 = (total + test_) ** -1
print(total)
print(test_)
print(p_0)
