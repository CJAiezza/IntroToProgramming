#indentifiers cannot start with a digit, but can include them. They cannot have
#special symbols anywhere in them and cannot be from the list on 2.1.1 but can
#include them.
import sys
sys.stdout.write("Enter ID: ")
roleID=int(sys.stdin.readline())
sys.stdout.write("Enter ID "+str(roleID)+"'s role: ")
role=sys.stdin.readline().strip()
sys.stdout.write("Hello "+role+" 00"+str(roleID))
