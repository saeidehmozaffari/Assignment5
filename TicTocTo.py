#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import colorama
import time
def show(game):
    for i in range(3):
        for j in range(3):
            if game[i][j]=='x':
                print(colorama.Fore.BLUE+game[i][j],end=' ')
            elif game[i][j]=='o':
                print(colorama.Fore.RED+game[i][j],end=' ')
        print()
def check(game):
    for i in range(3):
        if game[i][0]=='x' and game[i][1]=='x' and game[i][2]=='x':
            print(colorama.Fore.BLACK+'بازیکن اول برنده شد')
            print("Run Time: " + str( time.time() - start ))
            exit()
        if game[i][0]=='o' and game[i][1]=='o' and game[i][2]=='o':
            print(colorama.Fore.BLACK+'بازیکن دوم برنده شد')
            print("Run Time: " + str( time.time() - start ))
            exit()
        if game[0][i]=='o' and game[1][i]=='o' and game[2][i]=='o':
            print(colorama.Fore.BLACK+'بازیکن دوم برنده شد')
            print("Run Time: " + str( time.time() - start ))
            exit()
        if game[0][i]=='x' and game[1][i]=='x' and game[2][i]=='x':
            print(colorama.Fore.BLACK+'بازیکن اول برنده شد')
            print("Run Time: " + str( time.time() - start ))
            exit()
    if game[0][0] == 'x' and game[1][1] == 'x' and game[2][2] == 'x':
        print (colorama.Fore.BLACK+'بازیکن اول برنده شد')
        print("Run Time: " + str( time.time() - start ))
        exit ()
    if game[0][0]=='o' and game[1][1]=='o' and game[2][2]=='o':
        print('بازیکن دوم برنده شد')
        print("Run Time: " + str( time.time() - start ))
        exit()
    if game[0][2] == 'x' and game[1][1] == 'x' and game[2][0] == 'x':
        print (colorama.Fore.BLACK+'بازیکن اول برنده شد')
        print("Run Time: " + str( time.time() - start ))
        exit ()
    if game[0][2] == 'o' and game[1][1] == 'o' and game[2][0] == 'o':
        print (colorama.Fore.BLACK+'بازیکن اول برنده شد')
        print("Run Time: " + str( time.time() - start ))
        exit ()



game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]
show(game)
while True:
    x=int(input('اگربازی دونفره میخواهید انجام دهید عدد دو و گرنه یک را انتخاب کنید'))
    if x ==2 or x==1:
        break
while True:
    start = time.time()
    print(colorama.Fore.BLACK+'نوبت بازیکن اول')
    while True:
        row=int(input('enter row:'))
        col=int(input('enter col:'))
        if row<0 or row>2 or col<0 or col>2 or game[row][col]!='-':
            print('اشتباه')
        else:
            break
    game[row][col]='x'
    show(game)
    check(game)

    while True:
        if x==2:
            print (colorama.Fore.BLACK+'نوبت بازیکن دوم')
            row=int(input('enter row:'))
            col=int(input('enter col:'))
        if x==1:
            print (colorama.Fore.BLACK+'نوبت سیستم')
            row=random.randint(0,3)
            col=random.randint(0,3)
        if col not in range(3) or row not in range(3) or game[row][col]!='-':
           print(colorama.Fore.BLACK+'اشتباه')
        else:
            break
    game[row][col]='o'
    show(game)
    check(game)


# In[ ]:




