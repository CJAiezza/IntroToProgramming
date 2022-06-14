import sys

countries = ["Italy", "United Kingdom", "France", "China", "Canada"]
pasttimes = ["playing the guitar", "driving", "eating pizza", "using a computer", "watching Star Wars"]

lists = countries or pasttimes

w=0
while(w<len(lists)):
    sys.stdout.write(countries[w]+" "+str(len(countries[w])) + "\n")    
    sys.stdout.write(pasttimes[w]+" "+str(len(pasttimes[w])) + "\n")
    w+=1
