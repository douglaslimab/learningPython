from random import randint
from time import sleep

numbers = list()

def sortIt():
    for i in range(0, 5):
        numbers.append(randint(0, 99))
        print(f'{numbers[-1]} ', end='')
        sleep(1)
    print()

def sumEven(* num):
    result = 0
    for i in numbers:
        if (i % 2) == 0:
            result += i
    print(result)

# main
sortIt()
sumEven(numbers)