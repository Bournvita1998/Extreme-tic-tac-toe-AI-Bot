import random
import datetime
import copy

class Team3:

    def __init__(self):
        self.util ={}
        self.arr= [0.2,1,2,5,20]
        self.begin=0
        self.timelimit = datetime.timedelta(seconds=15.8)
        self.depthi=4
        pass

    def timer1(self,a):
        if a - self.begin <= self.timelimit:
            return False
        else:
            return True

    def notflag(self,flag):
        if flag != 'o':
            return 'o'
        if flag=='o':
            return 'x'

    def countutility(self,board,flag,depth):
        utility=0
        for i in range(4):
            for j in range(4):
                if board.block_status[i][j] == self.notflag(flag):
                    utility-=20
                if board.block_status[i][j] == flag:
                    utility+=20
                if board.block_status[i][j] == '-':
                    temp = [[0 for y in range(4)] for x in range(4)]
                    for x in range(4):
                        for y in range(4):
                            temp[x][y]=board.board_status[4*i+x][4*j+y] 
                    temp1 = [[board.board_status[(4*i+x)][(4*j+y)] for y in range(4) ] for x in range(4)]
                    utility -= self.updateutility(temp,self.notflag(flag))
                    utility += self.updateutility(temp,flag)

        utility-= 10*self.updateutility(board.block_status,self.notflag(flag))+0.01*depth
        utility+= 10*self.updateutility(board.block_status,flag)-0.01*depth
        return utility

    def updateutility(self,block,flag):
        cpblock = tuple([ tuple(block[i]) for i in range(4)])
        hrvalue=0
        if (cpblock,flag) in self.util:
            return self.util[cpblock, flag]
        else:
            topv=[(3,3),(0,3),(0,0),(3,0)]
            lowv=[(1,3),(2,3),(0,1),(3,1),(0,2),(2,0),(3,2),(1,0),(2,2),(1,1),(2,1),(1,2)]

            oflag = self.notflag(flag)

            count=0
            ocount=0

            if block[0][1] == flag:
                count += 1
            elif block[0][1] == oflag or block[0][1] == 'd':
                ocount += 1

            if block[1][0] == flag:
                count += 1
            elif block[1][0] == oflag or block[1][0] == 'd':
                ocount += 1

            if block[2][1] == flag:
                count += 1
            elif block[2][1] == oflag or block[2][1] == 'd':
                ocount += 1

            if block[1][2] == flag:
                count += 1
            elif block[1][2] == oflag or block[1][2] == 'd':
                ocount += 1

            dvalue = 0
            tvalue = 0
            fvalue = 0
            if ocount == 0:
                if count == 2 :
                    dvalue = 1
                if count == 3 :
                    tvalue = 1
                if count == 4 :
                    fvalue = 1
            hrvalue += dvalue* 2+ tvalue * 5 + fvalue * 20


            count=0
            ocount=0
            if block[0][2] == flag:
                count += 1
            elif block[0][2] == oflag or block[0][2] == 'd':
                ocount += 1

            if block[1][1] == flag:
                count += 1
            elif block[1][1] == oflag or block[1][1] == 'd':
                ocount += 1

            if block[2][2] == flag:
                count += 1
            elif block[2][2] == oflag or block[2][2] == 'd':
                ocount += 1

            if block[1][3] == flag:
                count += 1
            elif block[1][3] == oflag or block[1][3] == 'd':
                ocount += 1

            dvalue = 0
            tvalue = 0
            fvalue = 0
            if ocount == 0:
                if count == 2 :
                    dvalue = 1
                if count == 3 :
                    tvalue = 1
                if count == 4 :
                    fvalue = 1
            hrvalue += dvalue* 2+ tvalue * 5 + fvalue * 20


            count=0
            ocount=0
            if block[1][1] == flag:
                count += 1
            elif block[1][1] == oflag or block[1][1] == 'd':
                ocount += 1

            if block[2][0] == flag:
                count += 1
            elif block[2][0] == oflag or block[2][0] == 'd':
                ocount += 1

            if block[3][1] == flag:
                count += 1
            elif block[3][1] == oflag or block[3][1] == 'd':
                ocount += 1

            if block[2][2] == flag:
                count += 1
            elif block[2][2] == oflag or block[2][2] == 'd':
                ocount += 1

            dvalue = 0
            tvalue = 0
            fvalue = 0
            if ocount == 0:
                if count == 2 :
                    dvalue = 1
                if count == 3 :
                    tvalue = 1
                if count == 4 :
                    fvalue = 1
            hrvalue += dvalue* 2+ tvalue * 5 + fvalue * 20


            count=0
            ocount=0
            if block[1][2] == flag:
                count += 1
            elif block[1][2] == oflag or block[1][2] == 'd':
                ocount += 1

            if block[2][1] == flag:
                count += 1
            elif block[2][1] == oflag or block[2][1] == 'd':
                ocount += 1

            if block[3][2] == flag:
                count += 1
            elif block[3][2] == oflag or block[3][2] == 'd':
                ocount += 1

            if block[2][3] == flag:
                count += 1
            elif block[2][3] == oflag or block[2][3] == 'd':
                ocount += 1

            dvalue = 0
            tvalue = 0
            fvalue = 0
            if ocount == 0:
                if count == 2 :
                    dvalue = 1
                if count == 3 :
                    tvalue = 1
                if count == 4 :
                    fvalue = 1
            hrvalue += dvalue* 2+ tvalue * 5 + fvalue * 20

            count=0
            ocount=0
            for i in range(4):

                count=0
                ocount=0
                dvalue=0
                tvalue=0
                fvalue=0
                for j in range(4):
                    if block[j][i] == flag:
                        count +=1
                    elif block[j][i] == oflag or block[j][i] == 'd':
                        ocount +=1
                dvalue = 0
                tvalue = 0
                fvalue = 0
                if ocount == 0:
                    if count == 2:
                        dvalue =1
                    elif count == 3:
                        tvalue =1
                    elif count == 4:
                        fvalue =1
                hrvalue += dvalue* 2+ tvalue * 5 + fvalue * 20

                count=0
                ocount=0
                dvalue=0
                tvalue=0
                fvalue=0
                for j in range(4):
                    if block[i][j] == flag:
                        count +=1
                    elif block[i][j] == oflag or block[i][j] == 'd':
                        ocount +=1
                dvalue = 0
                tvalue = 0
                fvalue = 0
                if ocount == 0:
                    if count== 2:
                        dvalue =1
                    elif count == 3:
                        tvalue =1
                    elif count == 4:
                        fvalue =1
                hrvalue += dvalue* 2+ tvalue * 5 + fvalue * 20

            for val in lowv:
                if block[val[0]][val[1]] == flag:
                    hrvalue += 0.5*0.2
            for val in topv:
                if block[val[0]][val[1]] == flag:
                    hrvalue += 0.2
            self.util[cpblock,flag] = hrvalue
            return hrvalue

    def minimax(self,board,old_move,alpha,beta,maxim,flag,depthi,depth,initial):

        if self.timer1(datetime.datetime.utcnow()):
            return (0,(-1,-1))

        cells = board.find_valid_move_cells(old_move)
        states = board.find_terminal_state()

        if len(cells)==0:
            value = self.countutility(board,flag,depth)
            return (value,old_move)

        if depthi == depth:
            value = self.countutility(board,flag,depth)
            return (value,old_move)

        if states[1] == 'WON':
            if states[0] == flag:
                return (555,old_move)
            return(-555,old_move)

        random.shuffle(cells)
        for cell in cells:
            if maxim != 1:
                board.update(old_move,cell,self.notflag(flag))
                value = self.minimax(board,cell,alpha,beta,1,flag,depthi,depth+1,initial)
                u2=0
                if board.block_status[cell[0]%4][cell[1]%4]!='-':
                    u2=0.01
                if value[0]+u2 < beta:
                    beta = value[0]+u2
                    initial = cell
                if self.timer1(datetime.datetime.utcnow()):
                    board.block_status[cell[0]/4][cell[1]/4] = '-'
                    board.board_status[cell[0]][cell[1]] = '-'
                    return (0,(-1,-1))
                board.block_status[cell[0]/4][cell[1]/4] = '-'
                board.board_status[cell[0]][cell[1]] = '-'
            if maxim==1:
                board.update(old_move,cell,flag)
                value = self.minimax(board,cell,alpha,beta,0,flag,depthi,depth+1,initial)
                u2=0
                if board.block_status[cell[0]%4][cell[1]%4]!='-':
                    u2=-0.01
                if value[0]+u2 > alpha:
                    alpha = value[0]+u2
                    initial = cell
                if self.timer1(datetime.datetime.utcnow()):
                    board.block_status[cell[0]/4][cell[1]/4] = '-'
                    board.board_status[cell[0]][cell[1]] = '-'
                    return (0,(-1,-1))
                board.block_status[cell[0]/4][cell[1]/4] = '-'
                board.board_status[cell[0]][cell[1]] = '-'
            if alpha >= beta:
                break
        if maxim!=1:
            return (beta,initial)
        return (alpha,initial)


    def move(self,board,old_move,flag):
        self.begin = datetime.datetime.utcnow()
        self.timelimit = datetime.timedelta(seconds=15.8)
        self.depthi = 3
        cells = board.find_valid_move_cells(old_move)
        yo = random.randint(0,len(cells)-1)
        index = cells[yo]
        while not(self.timer1(datetime.datetime.utcnow())) and self.depthi<8:
            optimal = self.minimax(board,old_move,-1000000000,1000000000,1,flag,self.depthi,0,(6,6))
            if optimal[1]!=(-1,-1):
                index = optimal[1]
            self.depthi+=1
        return index