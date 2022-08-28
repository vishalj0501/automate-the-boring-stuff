import random
numberOfStreaks = 0

streak_list=[]
for experimentNumber in range(10000):
    for i in range (0,100):
        num=random.randint(0,1)
        streak_list.append(num)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(0,100):
        if (streak_list[i:i+7]==[0,0,0,0,0,0]) or (streak_list[i:i+7]==[1,1,1,1,1,1]):
            numberOfStreaks+=1


print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))