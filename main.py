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