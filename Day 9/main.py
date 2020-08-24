#!/bin/python3
#calculo de fatorial
def factorial(n):
    soma = 1
    for num in range(2, n + 1):
        soma *= num
    return soma