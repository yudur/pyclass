# criando pacotes e módulos em Python


def price_increase(value, percentage):
    v = value + (percentage / 100 * value)
    return v


def salary_reduction(value, percentage):
    v = value - (percentage / 100 * value)
    return v


if __name__ == '__main__':
    print(price_increase(100, 50))
    print(salary_reduction(100, 50))
