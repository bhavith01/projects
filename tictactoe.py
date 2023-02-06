xval = [0,0,0,0,0,0,0,0,0]
zval = [0,0,0,0,0,0,0,0,0]

count=0

def board():
    zero = 'X' if(xval[0]) else ('O' if(zval[0]) else '0')
    one = 'X' if(xval[1]) else ('O' if(zval[1]) else '1')
    two = 'X' if(xval[2]) else ('O' if(zval[2]) else '2')
    three= 'X' if(xval[3]) else ('O' if(zval[3]) else '3')
    four= 'X' if(xval[4]) else ('O' if(zval[4]) else '4')
    five = 'X' if(xval[5]) else ('O' if(zval[5]) else '5')
    six = 'X' if(xval[6]) else ('O' if(zval[6]) else '6')
    seven = 'X' if(xval[7]) else ('O' if(zval[7]) else '7')
    eight= 'X' if(xval[8]) else ('O' if(zval[8]) else '8')
    
    print(" "+zero+" | "+one+" | "+two )
    print("---|---|---")
    print(" "+three+" | "+four+" | "+five )
    print("---|---|---")
    print(" "+six+" | "+seven+" | "+eight )
    print("\n")

    
def checkforwin(win):
    winlist = [[0,1,2],[3,4,5],[5,7,8],[0,3,5],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in winlist:
        sum=0
        for j in i:
            sum=sum+win[j]
        if(sum==3):
            print("____________________________________")
            return 1
    
flag=0
print("Welcome to TicTacToe")
print("look at the numbers in the matrix , the numbers are the avaible moves")
board()
while(count<9):
    if(checkforwin(xval)):
        print("---___X is the WINNER___---")
        flag=1
        break
    elif(checkforwin(zval)):
        print("---___Y is the WINNER___---")
        flag=1
        break
    elif(count%2==0):
        print("TURN : player X \n")
        xInput = int(input("Enter your move\n"))
        xval[xInput]=1
        count=count+1
        board()
    else:
        print("TURN : player Y \n")
        zInput = int(input("Enter your move\n"))
        zval[zInput]=1
        count=count+1
        board()
        
if(flag==0):        
    print("its a draw")
    
        
    