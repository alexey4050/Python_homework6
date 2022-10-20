# Сфомировать список из N членов последовательности.
# Для N = 5:1,-3,9,-27,81 и т.д.

from random import randint

def get_degree(n):
    return[((-3)**i) for i in range(n)]

n = randint(1, 20)
print(get_degree(n))