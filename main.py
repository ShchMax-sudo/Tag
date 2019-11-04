from random import randint

def show(a, win):
    global x, y
    print('▓' * 13)
    for i in a:
        for j in i:
            if j == 16 and not win:
                print("▓  ", end='')
            else:
                print("▓", j, ' ' * (1 - j // 10), sep='', end='')
        print('▓')
        print('▓' * 13)
 

def MoveRight():
    global x, y, win, a
    if (not win):
        if (x == 3):
            return
        else:
            a[x + 1][y], a[x][y] = a[x][y], a[x + 1][y]
            x += 1
            if (checker()):
                win = True
            show(a, win)
 
def MoveLeft():
    global x, y, win, a
    if (not win):
        if (x == 0):
            return
        else:
            a[x - 1][y], a[x][y] = a[x][y], a[x - 1][y]
            x -= 1
            if (checker()):
                win = True
            show(a, win)
 
def MoveDown():
    global x, y, win, a
    if (not win):
        if (y == 3):
            return
        else:
            a[x][y + 1], a[x][y] = a[x][y], a[x][y + 1]
            y += 1
            if (checker()):
                win = True
            show(a, win)
 
def MoveUp():
    global x, y, win, a
    if (not win):
        if (y == 0):
            return
        else:
            a[x][y - 1], a[x][y] = a[x][y], a[x][y - 1]
            y -= 1
            if (checker()):
                win = True
            show(a, win)


a = [list([0] * 4) for i in range(4)]
for i in range(4):
    for j in range(4):
        a[i][j] = i * 4 + (j + 1)

def swap(xS, yS, xE, yE):
    t = a[xS][yS]
    a[xS][yS] = a[xE][yE]
    a[xE][yE] = t

def shuf():
    cX = 3
    cY = 3
    for i in range(200):
        mX = randint(-1,1)
        mY = randint(-1,1)
                  
        if cX >= 3:
            mX = randint(-1,0)
        if cX <= 0:
            mX = randint(0, 1)

        
        if cY >= 3:
            mY = randint(-1, 0)
        if cY <= 0:
            mY = randint(0, 1)
        
        swap(cX + mX, cY + mY, cX, cY)
        cX += mX
        cY += mY

shuf()
