import sys

a, b = 0, 1

while a < 10:
    sys.stdout.write(str(a))
    a, b = b, a+b

#convert print to sys.stdout.write for "for" and "in"
words = ["cat", "frog", "rabbit"]

for w in words:
  sys.stdout.write(w+" "+str(len(w))+ "\n")

#convert print to sys.stdout.write for "for" and "in" for "range"

a = ["Mary", "had", "a", "little", "lamb"]

for i in range(len(a)):
    sys.stdout.write(str(i)+" "+(a[i])+"\n") 
