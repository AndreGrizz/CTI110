# CTI-110
# P4HW1 - Score List
# Grissett
# 4/1/2022
#

def main():
      #This program takes a number grade and outputs a letter grade.
      #system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
  # F_score = 50

# Ask user for grade input      
# To Do: define the rest of the scores
    scores = []
    howmany = int(input('How many scores do you want to enter? '))
    print()
    
    for c in range(howmany):
        score = (int(input('Enter score #'+ str(c+1) +' : ')))
        while not 0 <= score <= 100 :
         print()
         
         score = int(input('''INVALD Score entered!!!!
Score should be between 0 and 100
Enter score #'''+ str(c+1) + ' again: '))
        scores.append(score)

                   
    Results = ('---------Results----------')
    lowest = min(scores)
    scores.remove(min(scores))
    average = sum(scores) / len(scores)

    print()
    print()
    print(Results)
    print('Lowest Score: ' , lowest) 
    print('Modified List: ' , scores) 
    print('Scores Average: ', average)
    if average >= A_score:
        print('Grade     : A')
    elif average >= B_score:
        print('Grade     : B')
    elif average >= C_score:
        print('Grade     : C')
    elif average >= D_score:
        print('Grade     : D')
    else:
        print('Grade     : F')
    print('--------------------------')

#program start
main()




