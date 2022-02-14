# How many studentts do you want to order pizza for ? 26
#2/13/2022
#CTI-110 P1HW2 -Pizza Order
#Andre Grissett
#How many students do you want to order pizza for = int(input())
NumStudent = int(input('How many students do you want to order pizza for ?'))
Total_slices = NumStudent * 3 
Total_Pizzas = NumStudent / 2


print()
print('----Pizza Order--------')
print('Number of Students:',NumStudent)
print('Pizza Slices Needed:',Total_slices)
print('Pizza Needed :',Total_Pizzas)
print('--------------------------')
