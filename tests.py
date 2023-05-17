# import math
#
# count = 0
# total = 0
# n = 3
# m = 5
# tao = 1.262
#
# count = 0
# total = 0
# for count in range(n):
#     total += n ** count / math.factorial(count) * tao ** count
#
# factorial = math.factorial(n)
# first = n ** n / factorial
# second = tao ** n + 1
# third = 1 - tao ** m
# fourth = 1 - tao
# test_ = first * second * third
# test_2 = test_ / fourth
# p_0 = (total + test_2) ** -1
#
# while count <= n:
#     total += (n ** count / math.factorial(count)) * (tao ** count)
#     count += 1
#
# factorial = math.factorial(n)
# first = n ** n / factorial
# second = tao ** n + 1
# third = 1 - tao ** m
# fourth = 1 - tao
# test_ = first * second * third
# test_2 = test_ / fourth
# p_0 = (total + test_2) ** -1

lambda_quastion = input('Введите ламбду и тип времени (час, мин, сут) ПРИМЕР (30 сут) --- ')
lambda_, type_lambda = lambda_quastion.split(' ')
lambda_ = float(lambda_)

lambda_ = lambda_ / 24
print(lambda_)
lambda_ = lambda_ / 60
print(lambda_)