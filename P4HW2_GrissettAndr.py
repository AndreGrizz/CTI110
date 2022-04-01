# CTI-110
# P4HW2 - Pizza Order
# CTI-110 P3HW2 -Pizza Order
# Andre Grissett
# 4/1/2022
#

from decimal import ROUND_UP
import math


def main():
    NumStudent = int(input('How many students do you want to order pizza for? '))
    Numpeople = float(input('Enter number of people per pizza ( 1.5, 2 or 3): '))
    while not (Numpeople == float(1.5) or Numpeople == float(2) or Numpeople == float(3)):
        print()
        print ("""INVALID ENTRY!!!!
Should have entered 1.5, 2  or 3\n""")
        print()
        Numpeople = float(input('Enter number of people per pizza again. ( 1.5, 2 or 3): '))
        
    
    
    
    
    Total_slices = NumStudent * 3
        
    Total_Pizzas = NumStudent / Numpeople
    Total_Pizzas = math.ceil(Total_Pizzas)
    dollar = (Total_Pizzas * 5 * 1.06)

    print()
    print('------Pizza Order-------')
    print('Numbers of Students:',NumStudent)
    #print('Pizza Slices Needed:',Total_slices)
    print('Pizza Needed :',Total_Pizzas)
    print(f'Price ${dollar:.2f}')
    print('-------------------------')
    print()
    print('Would you like to run program again (y for yes):')
        

    
main()
