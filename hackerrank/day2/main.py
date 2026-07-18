#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    comida = meal_cost
    propina = meal_cost*(tip_percent/100)
    impuesto = meal_cost*(tax_percent/100)
    
    total = comida + propina + impuesto
    
    print(f'El monto a pagar en caja es: {round(total)}')    

if __name__ == '__main__':
    meal_cost = float(input("Digite el monto bruto de la comida (decimal): ").strip())

    tip_percent = int(input("Digite el porcentaje de la propina (entero): ").strip())

    tax_percent = int(input("Digite el porcentaje del impuesto (entero): ").strip())    

    solve(meal_cost, tip_percent, tax_percent)