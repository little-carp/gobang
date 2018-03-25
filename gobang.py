import pygame, random, math, tkinter
import numpy as np

X1=40;   X2=600
Y1=100;  Y2=660
LEN=40;  gobang_r=20; gobangboard=[]

def DrawGobangBoard(screen):
    color = [0,0,0];
    for i in range(15):
        pygame.draw.line(screen, color, (X1,Y1+LEN*i), (X2,Y1+LEN*i), 1)
        pygame.draw.line(screen, color, (X1+LEN*i,Y1), (X1+LEN*i,Y2), 1)
    
    pygame.draw.line(screen, color, (X1-4,Y1-4), (X2+4,Y1-4), 5)
    pygame.draw.line(screen, color, (X1-4,Y2+4), (X2+4,Y2+4), 5)
    pygame.draw.line(screen, color, (X1-4,Y1-4), (X1-4,Y2+4), 5)
    pygame.draw.line(screen, color, (X2+4,Y1-4), (X2+4,Y2+4), 5)
    
    pygame.draw.circle(screen, color, [X1+3*LEN,  Y1+3*LEN],  3, 0)
    pygame.draw.circle(screen, color, [X1+11*LEN, Y1+3*LEN],  3, 0)
    pygame.draw.circle(screen, color, [X1+3*LEN,  Y1+11*LEN], 3, 0)
    pygame.draw.circle(screen, color, [X1+11*LEN, Y1+11*LEN], 3, 0)
    pygame.draw.circle(screen, color, [X1+7*LEN,  Y1+7*LEN],  3, 0)

def Init(screen):
    screen.fill((227, 207, 87))
    DrawGobangBoard(screen)
    gobangboard.clear()
    for i in range(15):
        t = []
        for j in range(15):
            t.append(0)
        gobangboard.append(t)
    font = pygame.font.SysFont('simhei', 56)
    text = font.render("智能五子棋", True, [0,0,0])
    screen.blit(text, [180,15])
    
def Distance(x1, y1, x2, y2):
    return int(math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2)))
    
def Drop(p):
    x = p[0]; y = p[1]
    if x < X1-gobang_r or x > X2+gobang_r or y < Y1-gobang_r or y > Y2+gobang_r:
        return [x,y],False
    a = int((x-X1)/LEN)*LEN + X1
    b = int((y-Y1)/LEN)*LEN + Y1
    
    d1 = Distance(x, y, a, b)
    if d1<gobang_r:
        if gobangboard[int((a-X1)/LEN)][int((b-Y1)/LEN)] == 0:
            return [a,b],True
        else: return [a,b],False
    
    d2 = Distance(x, y, a, b+LEN)
    if d2<gobang_r:
        if gobangboard[int((a-X1)/LEN)][int((b+LEN-Y1)/LEN)] == 0:
            return [a,b+LEN],True
        else: return [a,b+LEN],False
    
    d3 = Distance(x, y, a+LEN, b)
    if d3<gobang_r:
        if gobangboard[int((a+LEN-X1)/LEN)][int((b-Y1)/LEN)] == 0:
            return [a+LEN,b],True
        else: return [a+LEN,b],False
    
    d4 = Distance(x, y, a+LEN, b+LEN)
    if d4<gobang_r:
        if gobangboard[int((a+LEN-X1)/LEN)][int((b+LEN-Y1)/LEN)] == 0:
            return [a+LEN,b+LEN],True
        else: return [a+LEN,b+LEN],False
    return [a,b],False

def getGobang(x, y, dire, dis):
    if dire == 1:
        x += dis
    elif dire == 2:
        x += dis
        y += dis
    elif dire == 3:
        y += dis
    elif dire == 4:
        x -= dis
        y += dis
    elif dire == 5:
        x -= dis
    elif dire == 6:
        x -= dis
        y -= dis
    elif dire == 7:
        y -= dis
    elif dire == 8:
        x += dis
        y -= dis
    if x<0 or y<0 or x>14 or y>14:
        return -2
    return gobangboard[x][y]

def Evaluate(x, y, player):
    value = 0
    for i in np.arange(1,9):
        if getGobang(x,y,i,1) == player and getGobang(x,y,i,2) == player         and getGobang(x,y,i,3) == player and getGobang(x,y,i,4) == player:
            value += 2000
            continue
        if getGobang(x,y,i,-1) == player and getGobang(x,y,i,1) == player         and getGobang(x,y,i,2) == player and getGobang(x,y,i,3) == player:
            value += 2000
            continue
        if getGobang(x,y,i,-2) == player and getGobang(x,y,i,-1) == player         and getGobang(x,y,i,1) == player and getGobang(x,y,i,2) == player:
            value += 2000
            continue
        
        if getGobang(x,y,i,1) == player and getGobang(x,y,i,2) == player and getGobang(x,y,i,3) == player:
            if getGobang(x,y,i,-1) == 0:
                if getGobang(x,y,i,4) == 0:
                    value += 400
                    continue
                elif getGobang(x,y,i,4) == -player or getGobang(x,y,i,4) == -2:
                    value += 210
                    continue
            elif (getGobang(x,y,i,-1) == -player or getGobang(x,y,i,-1) == -2) and getGobang(x,y,i,4) == 0:
                value += 210
                continue
        
        if getGobang(x,y,i,-1) == player and getGobang(x,y,i,1) == player and getGobang(x,y,i,2) == player:
            if getGobang(x,y,i,-2) == 0:
                if getGobang(x,y,i,3) == 0:
                    value += 400
                    continue
                elif getGobang(x,y,i,3) == -player or getGobang(x,y,i,3) == -2:
                    value += 210
                    continue
            elif (getGobang(x,y,i,-2) == -player or getGobang(x,y,i,-2) == -2) and getGobang(x,y,i,3) == 0:
                value += 210
                continue
        
        if getGobang(x,y,i,1) == player and getGobang(x,y,i,2) == player:
            if getGobang(x,y,i,-1) == 0:
                if getGobang(x,y,i,3) == 0:
                    value += 110
                    continue
                elif (getGobang(x,y,i,3) == -player or getGobang(x,y,i,3) == -2)                 and (getGobang(x,y,i,-2) == 0 or getGobang(x,y,i,-2) == player):
                    value += 25
                    continue
            elif (getGobang(x,y,i,-1) == -player or getGobang(x,y,i,-1) == -2) and getGobang(x,y,i,3) == 0             and (getGobang(x,y,i,4) == 0 or getGobang(x,y,i,4) == player):
                value += 25
                continue
        
        if getGobang(x,y,i,-1) == player and getGobang(x,y,i,1) == player:
            if getGobang(x,y,i,-2) == 0:
                if getGobang(x,y,i,2) == 0:
                    value += 110
                    continue
                elif (getGobang(x,y,i,2) == -player or getGobang(x,y,i,2) == -2)                 and (getGobang(x,y,i,-3) == 0 or getGobang(x,y,i,-3) == player):
                    value += 25
                    continue
            elif (getGobang(x,y,i,-2) == -player or getGobang(x,y,i,-2) == -2) and getGobang(x,y,i,2) == 0             and (getGobang(x,y,i,3) == 0 or getGobang(x,y,i,3) == player):
                value += 25
                continue
                
        if getGobang(x,y,i,-1) == player:
            if getGobang(x,y,i,1) == 0 and (getGobang(x,y,i,-2) == 0             or getGobang(x,y,i,-2) == -player or getGobang(x,y,i,-2) == -2):
                value += 5
                continue
            elif getGobang(x,y,i,1) == -player or getGobang(x,y,i,1) == -2:
                value += 1
                continue
    return value
    
def getMaxValue(player):
    maxvalue=0;
    x = []; y = []
    for i in range(15):
        for j in range(15):
            if gobangboard[i][j] == 0:
                weight = Evaluate(i,j,player)
                if maxvalue < weight:
                    maxvalue = weight
                    x.clear(); y.clear()
                    x.append(i)
                    y.append(j)
                elif maxvalue == weight:
                    x.append(i)
                    y.append(j)
    t = random.randint(0,len(x)-1)
    xx = X1+x[t]*LEN
    yy = Y1+y[t]*LEN
    return maxvalue,[xx,yy]

def Win(turn):
    player = 1 if turn else -1
    for i in range(15):
        for j in range(11):
            if gobangboard[i][j] == player and gobangboard[i][j+1] == player and gobangboard[i][j+2] == player             and gobangboard[i][j+3] == player and gobangboard[i][j+4] == player:
                return True
    for i in range(15):
        for j in range(11):
            if gobangboard[j][i] == player and gobangboard[j+1][i] == player and gobangboard[j+2][i] == player             and gobangboard[j+3][i] == player and gobangboard[j+4][i] == player:
                return True
    for i in range(11):
        for j in range(11):
            if gobangboard[i][j] == player and gobangboard[i+1][j+1] == player and gobangboard[i+2][j+2] == player             and gobangboard[i+3][j+3] == player and gobangboard[i+4][j+4] == player:
                return True
    for i in range(11):
        for j in np.arange(4,15):
            if gobangboard[i][j] == player and gobangboard[i+1][j-1] == player and gobangboard[i+2][j-2] == player             and gobangboard[i+3][j-3] == player and gobangboard[i+4][j-4] == player:
                return True
    return False

def Tie():
    for i in range(15):
        for j in range(15):
            if gobangboard[i][j] == 0:
                return False
    return True

def showMessage(info, color):
    win = tkinter.Tk()
    win.wm_attributes('-topmost', 1)
    win.geometry("150x150")
    win.resizable(0,0)
    win.title("游戏结束")
    frame = tkinter.Frame(win, width='150', height='150', bg='#E3CE57')
    label = tkinter.Label(frame, text=info, bitmap= 'warning', compound='left', font='12',bg='#E3CE57', fg=color).pack(padx='20', pady='20')
    btn = tkinter.Button(frame, text="再玩一局！", command=win.destroy, bg='#E3CE57', fg=color).pack(padx='40', pady='20')
    frame.pack()
    win.mainloop()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,700), 0, 32)
    pygame.display.set_caption("Gobang, named betaFish, developed by cjy")
    while True:
        pygame.display.init()
        Init(screen)
        turn = True; flag = False
        while True:
            if turn == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        p = pygame.mouse.get_pos()
                        p,judge = Drop(p)
                        if judge == False:
                            flag = True
                            break
                        pygame.draw.circle(screen, [0,0,0], p, gobang_r, 0)
                        gobangboard[int((p[0]-X1)/LEN)][int((p[1]-Y1)/LEN)] = 1
                        turn = False
            else:
                max1,p1 = getMaxValue(-1)
                max2,p2 = getMaxValue(1)
                if max1>=max2 or max1>=10 and max2<220:
                    p = p1
                else:
                    p = p2
                pygame.draw.circle(screen, [255,255,255], p,  gobang_r, 0)
                gobangboard[int((p[0]-X1)/LEN)][int((p[1]-Y1)/LEN)] = -1
                turn = True
            pygame.display.update()
            if flag == True:
                flag = False
                continue
            if Win(not turn) == True:
                if turn == False:
                    showMessage('你赢了！', 'green')
                else:
                    showMessage('你输了！', 'red')
                break
            if Tie() == True:
                showMessage('双方平局！', 'yellow')
                break
            
if __name__ == "__main__":
    main()
