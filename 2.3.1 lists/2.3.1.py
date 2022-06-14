##import sys
##
##countries = ["Italy", "United Kingdom", "France", "China", "Canada"]
##pasttimes = ["playing the guitar", "driving", "eating pizza", "using a computer", "watching Star Wars"]
##
##lists = countries + pasttimes
##
##for w in lists:
##    
##    sys.stdout.write(w+" "+str(len(w)) + "\n")

import sys

names = {"Chris": 42, "Bobby": 39, "Nate": 44, "Frank": 38}

for name, age in names.copy().items():
        if age <=40:
         pass
        else:
            sys.stdout.write(name +"," +" you are over the hill." "\n")
         
