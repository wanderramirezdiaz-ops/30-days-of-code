#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input('El tamaño del arreglo:').strip())
    arr = list(map(int, input().rstrip().split()))
    
    # Invertir la lista e imprimirla separada por espacios
    print(*arr[::-1])