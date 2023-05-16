import math
def transfer_t_to_mui():

    ''' перевод t в mui '''

    question = int(input('У нас известно интенсивность?(1 - да; 0 - нет) - '))
    if question == 1:
        mui = float(input('Введите интенсивность потока обслуживания - '))
        return mui
    else:
        t = int(input('Введите время обслуживания - '))
        mui = float(1/t)
        return mui


def tao_processing(n, mui, lambda_):
    tao = lambda_ / n * mui
    return tao




def limit_processing(n, m, tao):
    count = 0
    total = 0
    while count <= n:
        total += n**count / math.factorial(count) * tao**count

    p_0 = (total + n**n/math.factorial(n) * tao**n-1 * (1 - tao**m) / 1 - tao)**-1


def main():
    n = float(input('Введите количество каналов - '))
    m = float(input('Введите максимальное количество в очереди - '))
    lambda_ = float(input('Введите интенсивность входящего потока - '))
    mui = transfer_t_to_mui()
    tao = tao_processing(n, mui, lambda_)


if __name__ == '__main__':
    pass
