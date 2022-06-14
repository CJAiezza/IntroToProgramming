import sys
##def fib(n):
##    a, b = 0, 1
##    while a < n:
##        print(a, end=' ') 
##        a, b = b, a+b
##    print()

##def docstring ():
##    """Do nothing, but document it.
##
##    No, really. It doesn't do anything
##    """
##    pass
##
##sys.stdout.write(docstring.__doc__)
##

def display():
    sys.stdout.write("Enter your age. ")
    age = int(sys.stdin.readline().strip())
    sys.stdout.write("Your age is "+str(age))
display()
