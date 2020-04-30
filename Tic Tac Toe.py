a=[]
theBoard={'top-l': ' ','top-m': ' ','top-r': ' ',
          'mid-l': ' ','mid-m': ' ','mid-r': ' ',
          'bottom-l': ' ','bottom-m': ' ','bottom-r': ' '}

def printboard(theBoard):
    print(theBoard['top-l'], '|',  theBoard['top-m'], '|', theBoard['top-r'])
    print('---+---+---')
    print(theBoard['mid-l'], '|',  theBoard['mid-m'], '|', theBoard['mid-r'])
    print('---+---+---')
    print(theBoard['bottom-l'], '|',  theBoard['bottom-m'], '|', theBoard['bottom-r'])

print("Your inputs should be in this format --> top-l,top-m,top-r,mid-l,mid-m,mid-r,bottom-l,bottom-m,bottom-r")
turn = 'X'
for i in range(9):
    print("turn for " + turn + ". Move to which spapce?")
    move=input()
    while True:
        if theBoard[move]==' ':
            theBoard[move] = turn
            break
        else:
            print("No No... Dont try to be extra smart, give your ", turn, "elsewhere\n")
            move=input()
    if (turn == 'X'):
        if theBoard['top-l']==theBoard['top-m']==theBoard['top-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['mid-l']==theBoard['mid-m']==theBoard['mid-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['bottom-l']==theBoard['bottom-m']==theBoard['bottom-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['top-l']==theBoard['mid-l']==theBoard['bottom-l']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['top-m']==theBoard['mid-m']==theBoard['bottom-m']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['top-l']==theBoard['mid-l']==theBoard['bottom-l']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['top-l']==theBoard['mid-m']==theBoard['bottom-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        elif theBoard['top-r']==theBoard['mid-m']==theBoard['bottom-l']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is X')
            break
        turn = '0'
    else:
        if theBoard['top-l']==theBoard['top-m']==theBoard['top-r']!=' ':
            print('Winner is 0')
            break
        elif theBoard['mid-l']==theBoard['mid-m']==theBoard['mid-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is 0')
            break
        elif theBoard['bottom-l']==theBoard['bottom-m']==theBoard['bottom-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is 0')
            break
        elif theBoard['top-l']==theBoard['mid-l']==theBoard['bottom-l']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is 0')
            break
        elif theBoard['top-m']==theBoard['mid-m']==theBoard['bottom-m']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is 0')
            break
        elif theBoard['top-l']==theBoard['mid-l']==theBoard['bottom-l']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is 0')
            break
        elif theBoard['top-l']==theBoard['mid-m']==theBoard['bottom-r']!=' ':
            printboard(theBoard)
            a = 1
            print('Winner is 0')
            break
        elif theBoard['top-r']==theBoard['mid-m']==theBoard['bottom-l']!=' ':
            printboard(theBoard)
            a=1
            print('Winner is 0')
            break
        turn = 'X'
    printboard(theBoard)
    if (i==8 and a!=1):
        print("Draw match")