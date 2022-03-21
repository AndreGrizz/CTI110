#CTI-110
#P3HW1 _ Debugging
#Andre Grissett
# 3/20/2022

# I was supposed to put a comment here

def main():
      #This program takes a number grade and outputs a letter grade.
      #system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

# Ask user for grade input      
# To Do: define the rest of the scores

    Score = int(input('Please enter score: '))
    if Score >= A_score:
       print('Grade is A.')
    elif Score >= B_score:
        print('Grade is B.')
    elif Score >= C_score:
        print('Grade is C.')
    elif Score >= D_score:
        print('P3LAB1_GrissettAndre.py')
    else:
        print('Grade is F.') # To Do: Finish this

#program start
main()
