# Для натурального n создать словарь индекс-значения,
# состоящий из элементов последовательности 3n +1.

from random import randint

def get_dict(n):
    return{x: 3 * x + 1 for x in range(1, n+1)}

n = randint(5, 20)

print(n)
print(get_dict(n))