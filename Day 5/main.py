#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    c = 1
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
