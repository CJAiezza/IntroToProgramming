##import sys
##def getFibAt(i): #return Fibonacci series value at i
##   a, b=0, 1
##   while i>0:
##      a, b = b, a+b
##      i-=1
##   return a
##sys.stdout.write("Enter a position in the Fibonacci sequence: ")
##i = int( sys.stdin.readline() )
##answer = getFibAt(i)
##sys.stdout.write( str(answer)+" is at "+str(i))

import sys
def getMultipleAt(i): #get power of 2 value at i

    a = 1

    while i>0:
        a = a*2
        i-=1  
    return a
sys.stdout.write("Enter position of power of 2: ")
i = int (sys.stdin.readline() )
answer = getMultipleAt(i)
sys.stdout.write ( str(answer)+" is the "+str(i)  +" power of 2")

##import sys
##def getMultipleAt(i): #get multiple of 2 value at i
##   
##    a= i*2
##       
##    return a
##sys.stdout.write("Enter a number to multiply by two: ")
##i = int (sys.stdin.readline() )
##answer = getMultipleAt(i)
##sys.stdout.write ( str(answer)+" is "+str(i) +" times 2")
##
