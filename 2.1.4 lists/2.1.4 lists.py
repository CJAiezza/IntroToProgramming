import sys

countries = ["Italy", "United Kingdom", "France", "China", "Canada"]
pasttimes = ["playing the guitar", "driving", "eating pizza", "using a computer", "watching Star Wars"]

lists = countries + pasttimes

for w in lists:
    sys.stdout.write(w+" "+str(len(w)) + "\n")
