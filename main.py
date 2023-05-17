import math
from re import match


def transfer_t_to_mui():

    ''' перевод t в mui '''

    # question = int(input('У нас известно интенсивность?(1 - да; 0 - нет) - '))

    question = 1
    if question == 1:
        # mui = float(input('Введите интенсивность потока обслуживания - '))
        mui = 0.33
        print(f'\nmui = {mui}\n')

    else:
        t = int(input('Введите время обслуживания - '))
        mui = float(1/t)
        print(f'\nmui = {mui}\n')

    lambda_question = input('Введите ламбду и тип времени (час, мин, сут) ПРИМЕР (30 сут) --- ')
    lambda_, type_lambda = lambda_question.split(' ')
    float(lambda_)

    match type_lambda:
        case 'час':
            lambda_ /= 60
        case 'сут':
            lambda_ = lambda_ / 24
            print(lambda_)
            lambda_ = lambda_ / 60
            print(lambda_)




def tao_processing(n, mui, lambda_):
    one = n * mui
    tao = lambda_ / one
    print(f'tao = {tao}\n')
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
        print(keys, '=', values, '\n')

    return all_iteration


def relative_and_absolute(lambda_, all_iteration, n, m):

    Q = 1 - all_iteration[f'p_{n + m}']
    print(f'Q = {Q}\n')

    A = lambda_ * Q
    print(f'A = {A}\n')

    return A

def all_N_and_T(A, mui, tao, m, n, all_iteration, lambda_):

    N_s = A / mui
    print(f'N_s = {N_s}\n')

    one_N_line = n**n / math.factorial(n)
    two_N_line = one_N_line * tao**n+1
    some = 1 - tao**m
    three_N_line = some * (m + 1 - m * tao)
    four_N_line = 1 - tao
    five = three_N_line / four_N_line**2

    N_line = two_N_line * five * all_iteration['p_0']
    print(f'N_line = {N_line}\n')

    N = N_s + N_line
    print(f'N = {N}\n')


    T_s = N_s / lambda_
    print(f'T_s = {T_s}\n')

    T_line = N_line / lambda_
    print(f'T_line = {T_line}\n')

    T = T_s + T_line
    print(f'T = {T}\n')


def main():
    # n = float(input('Введите количество каналов - '))
    # m = float(input('Введите максимальное количество в очереди - '))
    # lambda_ = float(input('Введите интенсивность входящего потока - '))

    n = 3
    m = 5
    lambda_ = 1.25
    mui = transfer_t_to_mui()
    tao = tao_processing(n, mui, lambda_)
    all_iteration = limit_processing(n, m, tao)
    A = relative_and_absolute(lambda_, all_iteration, n, m)
    all_N_and_T(A, mui, tao, m, n, all_iteration, lambda_)

if __name__ == '__main__':
    main()
