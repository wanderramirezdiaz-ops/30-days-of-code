import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input('Digite un mumero entero:').strip())

    if N % 2 != 0:
        print("Estoy feliz ")
    elif N % 2 == 0 and 2 <= N <= 5:
        print("Dios es bueno")
    elif N % 2 == 0 and 6 <= N <= 20:
        print("Dios bendice")
    elif N % 2 == 0 and N > 20:
        print("NO BULTO")