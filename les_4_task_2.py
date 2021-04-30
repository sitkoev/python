import timeit
import cProfile
from math import e, log
'''
    функция возвращает i-й элемент ряда простых чисел
'''
def prime(i):
    prime_numbers = ([2, 3]) # начальный ряд простых чисел
    if i <= 2:
       return i
    else:
        spam = prime_numbers[-1]
        while True:
            prime = True # предположим, что число spam простое
            spam += 1
            for k in prime_numbers:
                if spam % k == 0 and k != 1: # проверка на наличие делителя из ряда простых чисел
                    prime = False   # число spam оказалось сложным
                    break           # поэтому цикл проверок прерывается
            if prime:
                prime_numbers.append(spam)
            if len(prime_numbers) == i:
                return prime_numbers[i - 1]
'''
применение алгоритма Эратосфена для вычисления i - го простого числа проблематизируется определением 
размера полигона для "продырявливания".
принимаю, что величина, полученная делением простого i-го числа Рi деленное на i не превышает ln(Pi)
'''
def calc_base(i): # расчет максимального значения базы для расчета i-го простого числа
    base = 10
    while True:
        if i > base/log(base, e):
            base = (base + base) * log(base, e) # домножаю на log(base, e) шобы прирастала быстрее
        else:
            return int(base)


def sieve(i, sieve, hole_assign):
    n = len(sieve)
    for k in range(2, n):
        if sieve[k] != hole_assign:
            j = k + k
            while j < n:
                sieve[j] = hole_assign
                j += k
    res = [item for item in sieve if item != hole_assign]
    return res[i - 1]


HOLE = 0
NUMBER_PRIME = 1000
n = calc_base(NUMBER_PRIME)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE

print(f'простой алгоритм: {prime(NUMBER_PRIME)} , решето Эратосфена: {sieve(NUMBER_PRIME, dim_sieve, HOLE)}')



print(timeit.timeit('prime(8)', number=1000, globals=globals()))    # 0.005260000000000001
print(timeit.timeit('prime(16)', number=1000, globals=globals()))   # 0.015145600000000002
print(timeit.timeit('prime(32)', number=1000, globals=globals()))   # 0.043249300000000004
print(timeit.timeit('prime(64)', number=1000, globals=globals()))   # 0.1399882
print(timeit.timeit('prime(128)', number=1000, globals=globals()))  # 0.4125564
print(timeit.timeit('prime(254)', number=1000, globals=globals()))  # 1.4607706999999999
print(timeit.timeit('prime(512)', number=1000, globals=globals()))  # 5.9072648
print(timeit.timeit('prime(1024)', number=1000, globals=globals())) # 23.4532957

print('====================================================================================================')
print('method sieve()')
n = calc_base(8)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(8,dim_sieve, HOLE)', number=1000, globals=globals())) # 0.006377300000000474
n = calc_base(16)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(16,dim_sieve, HOLE)', number=1000, globals=globals())) # 0.06603029999999777
n = calc_base(32)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(32,dim_sieve, HOLE)', number=1000, globals=globals())) # 0.0589694999999999
n = calc_base(64)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(64,dim_sieve, HOLE)', number=1000, globals=globals())) # 0.8232302000000011
n = calc_base(128)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(128,dim_sieve, HOLE)', number=1000, globals=globals())) # 0.8291494000000021
n = calc_base(254)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(254,dim_sieve, HOLE)', number=1000, globals=globals())) # 824268
n = calc_base(512)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(512,dim_sieve, HOLE)', number=1000, globals=globals())) # 15.725551
n = calc_base(1024)
dim_sieve = [k for k in range(n + 1)]
dim_sieve[1] = HOLE
print(timeit.timeit('sieve(1024,dim_sieve, HOLE)', number=1000, globals=globals())) # 15.682386300000005


cProfile.run('prime(512)')
'''
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.005    0.005    0.006    0.006 les_4_task_2.py:7(prime)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
     3668    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      510    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         6 function calls in 0.017 seconds
'''

dim_sieve = [k for k in range(calc_base(512))]
dim_sieve[1] = HOLE
cProfile.run('sieve(512,dim_sieve, HOLE)')
'''
 Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.017    0.017 <string>:1(<module>)
        1    0.016    0.016    0.017    0.017 les_4_task_2.py:38(sieve)
        1    0.002    0.002    0.002    0.002 les_4_task_2.py:46(<listcomp>)
        1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''

'''
Выводы:
    Сравнены 2 алгоритма вчисления i-го простого числа
    1. алгоритм prime(), основывается на классическом способе определения простого числа,
    имеет квадратичную ассимптотику
    2. алгоритм sieve(), основанный на принципе "Решето Эратосфена", имеет логарифмическую ассимптотику 
'''
