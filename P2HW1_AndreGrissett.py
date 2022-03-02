# A brief description of the project
# 2/28/2022
# CTI-110 P2HW1 - Total Purchases
# Andre Grissett


#Ask user to enter prices of 5 items
#Calculate Subtotal (total of all item prices entered)
#Calculate Sales tax of item prices entered
#Calculate overall total (subtotal + sales tax)

SALESTAX =.07
item1 = float(input('Enter the price of item #1: ',))
item2 = float(input('Enter the price of item #2: ',))
item3 = float(input('Enter the price of item #3: ',))
item4 = float(input('Enter the price of item #4: ',))
item5 = float(input('Enter the price of item #5: ',))


Results = '-------Results-------'
                
Subtotal = (item1 + item2 + item3 + item4 + item5)
Sale_Tax = (Subtotal * SALESTAX)
Total_Prices = (Subtotal + Sale_Tax)

print(Results)
print(f'Subtotal: {Subtotal:.2f}')
print(f'Sales Tax: {Sale_Tax:.2f}')
print(f'Total: {Total_Prices:.2f}')
