import sys

sys.stdout.write("What's your favourite colour?")
colour = sys.stdin.readline().strip()
sys.stdout.write("Your favourite colour is "+colour)
