import sys

AreYouaJedi = int(input("""Are you one with the force or do you deal in absolutes?
Enter number between 1 and 10:
Let's find out.
"""))
#Thanks go to Geoffrey Davis for the "input" command. 
                  
if AreYouaJedi >5 and AreYouaJedi <10:
    sys.stdout.write("You are a Jedi. Like my father before me.")
if AreYouaJedi <5:
    sys.stdout.write("You are a Sith. You were my brother Anakin!")
if AreYouaJedi ==5:
    sys.stdout.write("You are a nondenominational force user. You brought balance to the force.")
if not AreYouaJedi <10:
    sys.stdout.write("No, I don't want Death Sticks. Go home and rethink your life. ")
