#Pick a number from the list do run the Math Quiz
#4/21/2022
#CTI-110 P5HW2 - Math Quiz
#Andre Grissett
#

import random


def Generation():
   number = random.randint(1,100)
   return number


def addition():
   number1 = Generation()
   number2 = Generation()
   sum = number1 + number2
   print('  ' + str(number1) + '\n+ ' + str(number2))
   print()
   answer =input('Enter Answer \n')
   count = 1 
   while True:
      if int(answer) == sum:
         print('Congratulations!!!! your answer is correct..\nNumber of guessess: '+ str(count))
         print()
         break
      elif int(answer) > sum:
         answer = input('Sorry, guess is too high. \n\ntry again :')
         count = count + 1
      else:
         answer = input('Sorry, guess is too low. \n\ntry again: ')
         count = count + 1


def subtraction():
   number1 = Generation()
   number2 = Generation()
   diff = number1 - number2
   print('  '+str(number1) + '\n- ' + str(number2))
   answer =input('Enter Answer \n')
   count = 1 
   while True:
      if int(answer) == diff:
         print('Congratulations!!!! your answer is correct..\nNumber of guessess: '+ str(count))
         print()
         break
      elif int(answer) > diff:
         answer = input('Sorry, guess is too high. \n\ntry again : ')
         count = count + 1
      else:
         answer = input('Sorry, guess is too low. \n\ntry again: ')
         count = count + 1

def menu():
   print('Welcome to Math Quiz')
   print()
   print()
   while True:
      choice = input('MAIN MENU \n-------------------- \n1. Adding Random Numbers \n2. Subtracting Radom Numbers \n3. Exit \n\nPlease choose one of the menu options: ')
      if choice == '1':
         addition()
      elif choice == '2':
         subtraction()
      elif choice == '3':
         print('Thank you for playing... \nBye!!') 
         break
      else:
         print('Error : Please select from one of the options from the menu')
         print()



def main():
   menu()

main()   
   
