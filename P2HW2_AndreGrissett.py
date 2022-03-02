# CTI-110
# P2HW2-Score Avg
# Andre Grissett
#
#Enter score for the list
#Lowest score entered
#Modified List after dropping lowest score
#Average of scores in the modified list

item1 = int(input('Enter score #1: '))
item2 = int(input('Enter score #2: '))
item3 = int(input('Enter score #3: '))
item4 = int(input('Enter score #4: '))
item5 = int(input('Enter score #5: '))
item6 = int(input('Enter score #6: '))
item7 = int(input('Enter score #7: '))



Results = ('---------Results----------')


                
scores = [item1 , item2 , item3 , item4 , item5 , item6 , item7]
lowest = min(scores)
scores.remove(min(scores))
average = sum(scores) / len(scores)



print(Results)
print('Lowest Score: ' , min(scores))
print('Modified List: ' ,scores) 
print('Scores Average: ',average)
print('-----------------------------')
