import random
print('Welcome')
gameOver = False
side = True
draw = False
row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']
list1 = [0,0,0]
list2 = [0,0,0]
list3 = [0,0,0]
def result():
    print('-------------------')
    print(row1)
    print(row2)
    print(row3)
    print('-------------------')
def control():
    global gameOver, a, b, c, d, e, f, g, h, draw
    a = int(list1[0] + list1[1] + list1[2])
    b = int(list2[0] + list2[1] + list2[2])
    c = int(list3[0] + list3[1] + list3[2])
    d = int(list1[0] + list2[0] + list3[0])
    e = int(list1[1] + list2[1] + list3[1])
    f = int(list1[2] + list2[2] + list3[2])
    g = int(list1[0] + list2[1] + list3[2])
    h = int(list1[2] + list2[1] + list3[0])
    if a == 9 or b == 9 or c == 9 or d == 9 or e == 9 or f == 9 or g == 9 or h == 9:
        gameOver = True
        print('You WON!')
    elif a == 15 or b == 15 or c == 15 or d == 15 or e == 15 or f == 15 or g == 15 or h == 15:
        gameOver = True
        print('You LOST!')
    elif a + b + c == 35 and d + e + f == 35:
        gameOver = True
        print('It is DRAW!')
        draw = True
def bot():
    global side, list1, list2, list3, sar, sur, a, b, c, d, e, f, g, h, row1, row2, row3
    side = True
    if gameOver == False:
        if a == 10:
            if list1[0] == 0:
                list1[0] = 5
                row1[0] = 'X'
                result()
            elif list1[1] == 0:
                list1[1] = 5
                row1[1] = 'X'
                result()
            elif list1[2] == 0:
                list1[2] = 5
                row1[2] = 'X'
                result()
        elif b == 10:
            if list2[0] == 0:
                list2[0] = 5
                row2[0] = 'X'
                result()
            elif list2[1] == 0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list2[2] == 0:
                list2[2] = 5
                row2[2] = 'X'
                result()
        elif c == 10:
            if list3[0] == 0:
                list3[0] = 5
                row3[0] = 'X'
                result()
            elif list3[1] == 0:
                list3[1] = 5
                row3[1] = 'X'
                result()
            elif list3[2] == 0:
                list3[2] = 5
                row3[2] = 'X'
                result()
        elif d == 10:
            if list1[0] == 0:
                list1[0] = 5
                row1[0] = 'X'
                result()
            elif list2[0] == 0:
                list2[0] = 5
                row2[0] = 'X'
                result()
            elif list3[0] == 0:
                list3[0] = 5
                row3[0] = 'X'
                result()
        elif e == 10:
            if list1[1] == 0:
                list1[1] = 5
                row1[1] = 'X'
                result()
            elif list2[1] == 0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list3[1] == 0:
                list3[1] = 5
                row3[1] = 'X'
                result()
        elif f == 10:
            if list1[2] == 0:
                list1[2] = 5
                row1[2] = 'X'
                result()
            elif list2[2] == 0:
                list2[2] = 5
                row2[2] = 'X'
                result()
            elif list3[2] == 0:
                list3[2] = 5
                row3[2] = 'X'
                result()
        elif g == 10:
            if list1[0] == 0:
                list1[0] = 5
                row1[0] = 'X'
                result()
            elif list2[1] == 0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list3[2] == 0:
                list3[2] = 5
                row3[2] = 'X'
                result()
        elif h == 10:
            if list1[2] == 0:
                list1[2] = 5
                row1[2] = 'X'
                result()
            elif list2[1] == 0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list3[0] == 0:
                list3[0] = 5
                row3[0] = 'X'
                result()
        elif a == 6:
            if list1[0] == 0:
                list1[0]=5
                row1[0]='X'
                result()
            elif list1[1]==0:
                list1[1] = 5
                row1[1] = 'X'
                result()
            elif list1[2]==0:
                list1[2] = 5
                row1[2] = 'X'
                result()
        elif b == 6:
            if list2[0] == 0:
                list2[0]=5
                row2[0]='X'
                result()
            elif list2[1]==0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list2[2]==0:
                list2[2] = 5
                row2[2] = 'X'
                result()
        elif c == 6:
            if list3[0] == 0:
                list3[0]=5
                row3[0]='X'
                result()
            elif list3[1]==0:
                list3[1] = 5
                row3[1] = 'X'
                result()
            elif list3[2]==0:
                list3[2] = 5
                row3[2] = 'X'
                result()
        elif d == 6:
            if list1[0] == 0:
                list1[0]=5
                row1[0]='X'
                result()
            elif list2[0]==0:
                list2[0] = 5
                row2[0] = 'X'
                result()
            elif list3[0]==0:
                list3[0] = 5
                row3[0] = 'X'
                result()
        elif e == 6:
            if list1[1] == 0:
                list1[1]=5
                row1[1]='X'
                result()
            elif list2[1]==0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list3[1]==0:
                list3[1] = 5
                row3[1] = 'X'
                result()
        elif f == 6:
            if list1[2] == 0:
                list1[2]=5
                row1[2]='X'
                result()
            elif list2[2]==0:
                list2[2] = 5
                row2[2] = 'X'
                result()
            elif list3[2]==0:
                list3[2] = 5
                row3[2] = 'X'
                result()
        elif g == 6:
            if list1[0] == 0:
                list1[0]=5
                row1[0]='X'
                result()
            elif list2[1]==0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list3[2]==0:
                list3[2] = 5
                row3[2] = 'X'
                result()

        elif h == 6:
            if list1[2] == 0:
                list1[2]=5
                row1[2]='X'
                result()
            elif list2[1]==0:
                list2[1] = 5
                row2[1] = 'X'
                result()
            elif list3[0]==0:
                list3[0] = 5
                row3[0] = 'X'
                result()
        else:
            if list2[1] == 0:
                list2[1] == 5
                row2[1] == 'X'
                result()
            else:
                sar = random.randint(1, 3)
                sur = random.randint(1,3)
                sur -= 1
                if sar == 2 or sur == 1:
                    bot()
                else:
                    if sar == 1:
                        if row1[sur] == 'X' or row1[sur] == 'O':
                            bot()
                        else:
                            row1[sur] = 'X'
                            list1[sur] = 5
                            result()
                    elif sar == 2:
                        if row2[sur] == 'X' or row2[sur] == 'O':
                            bot()
                        else:
                            row2[sur] = 'X'
                            list2[sur] = 5
                            result()
                    elif sar == 3:
                        if row3[sur] == 'X' or row3[sur] == 'O':
                            bot()
                        else:
                            row3[sur] = 'X'
                            list3[sur] = 5
                            result()
        control()
    if gameOver == False:
        request()
def request():
    number = input()
    if number == '1' or number == '2' or number == '3' or number == '4' or number == '5' or number == '6' or number == '7' or number == '8' or number == '9':
        global side
        side = False
        if number == '1':
            if row1[0] == 'O' or row1[0] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row1[0] = 'O'
                list1[0] = 3
                result()
                control()
        elif number == '2':
            if row1[1] == 'O' or row1[1] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row1[1] = 'O'
                list1[1] = 3
                result()
                control()
        elif number == '3':
            if row1[2] == 'O' or row1[2] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row1[2] = 'O'
                list1[2] = 3
                result()
                control()
        elif number == '4':
            if row2[0] == 'O' or row2[0] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row2[0] = 'O'
                list2[0] = 3
                result()
                control()
        elif number == '5':
            if row2[1] == 'O' or row2[1] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row2[1] = 'O'
                list2[1] = 3
                result()
                control()
        elif number == '6':
            if row2[2] == 'O' or row2[2] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row2[2] = 'O'
                list2[2] = 3
                result()
                control()
        elif number == '7':
            if row3[0] == 'O' or row3[0] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row3[0] = 'O'
                list3[0] = 3
                result()
                control()
        elif number == '8':
            if row3[1] == 'O' or row3[1] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row3[1] = 'O'
                list3[1] = 3
                result()
                control()
        elif number == '9':
            if row3[2] == 'O' or row3[2] == 'X':
                print('!ERROR!')
                print('Please try to fill an empty section')
                request()
            else:
                row3[2] = 'O'
                list3[2] = 3
                result()
                control()
    else:
        print('!ERROR!')
        print('Incorrect entry')
        request()
    if gameOver == False:
        bot()
result()
print('Your turn')
request()