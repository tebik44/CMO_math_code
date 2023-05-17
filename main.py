import math
def transfer_t_to_mui():

    ''' перевод t в mui '''

    question = int(input('У нас известно интенсивность?(1 - да; 0 - нет) - '))
    if question == 1:
        mui = float(input('Введите интенсивность потока обслуживания - '))
        print(f'mui = {mui}')
        return mui
    else:
        t = int(input('Введите время обслуживания - '))
        mui = float(1/t)
        print(f'mui = {mui}')
        return mui


def tao_processing(n, mui, lambda_):
    one = n * mui
    tao = lambda_ / one
    print(f'tao = {tao}')
    return tao


def limit_processing(n, m, tao):
    count = 0
    total = 0
    for count in range(n):
        total += n**count / math.factorial(count) * tao**count


    factorial = math.factorial(n)
    first = n ** n / factorial
    second = tao ** n + 1
    third = 1 - tao ** m
    fourth = 1 - tao
    test_ = first * second * third
    test_2 = test_ / fourth
    p_0 = (total + test_2) ** -1

    sum_iteration = n + m
    all_iteration = dict()
    for k in range(sum_iteration + 1):
        if k <= n:
            one = n**k / math.factorial(k)
            all_iteration[f'p_{k}'] = one * tao**k * p_0
        else:
            two = n ** n / math.factorial(n)
            all_iteration[f'p_{k}'] = two * tao**k * p_0

    for keys, values in all_iteration.items():
        print(keys)
        print(values)




def main():
    # n = float(input('Введите количество каналов - '))
    # m = float(input('Введите максимальное количество в очереди - '))
    # lambda_ = float(input('Введите интенсивность входящего потока - '))

    n = 3
    m = 5
    lambda_ = 1.25
    mui = transfer_t_to_mui()
    tao = tao_processing(n, mui, lambda_)
    p_0 = limit_processing(n, m, tao)

if __name__ == '__main__':
    main()
