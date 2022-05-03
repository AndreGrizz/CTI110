# collect the score 
# 4/21/2022
# CTI-110 P5HW1 - Score List
# Andre Grissett
#

#This program takes a number grade and outputs a letter grade.
#system uses 10-point grading scale
#A_score = 90
#B_score = 80
#C_score = 70
#D_score = 60
# F_score = 50


def Menu():
      scores = []
      while True:
         choice = input('----------MENU ---------- \n1. Create Score List \n2. Display Results \n3. Exit \n------------------------ ')
         if choice == '1':
            scores = Score_Input()
         elif choice == '2':
            Display_Results(scores)
         elif choice == '3':
            print('Thank you for playing... \nBye!!')
            break
         else:
            print('Please make a choice from the \'MENU\'.')
            


# Ask user for grade input
def Score_Input():
   scores = []
   howmany = int(input('How many scores do you want to enter? '))
   print()
   for c in range(howmany):
      score = (int(input('Enter score '+ str(c+1) +' : ')))
      while not 0 <= score <= 100 :
         score = int(input('''INVALD Score entered!!!!
Score should be between 0 and 100
Enter score ''' + str(c+1) + ' again: '))
      scores.append(score)
   return(scores)
   
def Display_Results(scores):
   A_score = 90
   B_score = 80
   C_score = 70
   D_score = 60
   lowest = min(scores)
   scores.remove(min(scores))
   average = sum(scores) / len(scores)
   print()
   print()
   print('---------Results----------')
   print('Lowest Score: ' , lowest)
   print('Modified List: ' , scores)
   print('Scores Average: ', average)
   if average >= A_score:
      print('Grade : A')
   elif average >= B_score:
      print('Grade : B')
   elif average >= C_score:
      print('Grade: C')
   elif average >= D_score:
      print('Grade : D')
   else:
      print('Grade : F')
   print('--------------------------')


def Main ():
   Menu()




#program start
Main()
