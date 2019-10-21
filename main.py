

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
