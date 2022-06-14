import sys

#ask user for given and sur-name.
sys.stdout.write("Enter your first name: ")
firstname = sys.stdin.readline().strip()
sys.stdout.write("Enter your last name: ")
surname = sys.stdin.readline().strip()
#greet user
sys.stdout.write("Hello There, General " +firstname+ " " +surname+ ". You are a bold one.")

#ask user for age convert number to string. prgram crashes if a float is entered. I need to debug.
sys.stdout.write("\n \nHow old are you? ")
value = int(sys.stdin.readline().strip())

#If they enter a negative number, they get asked to reinput.
while value < 0:
        sys.stdout.write("You're not born yet " +firstname+ " " +surname+ ", try again.\n")
        value = int(sys.stdin.readline().strip())

if value <42:
        sys.stdout.write("Oh You are still young compared to me " +firstname+ " " +surname+ ".\n")

if value ==42:
        sys.stdout.write("You are the same age as me " +firstname+ " " +surname+ ".\n")

if value >42:
    sys.stdout.write("You are older than me " +firstname+ " " +surname+ ".\n")

    
#ask user for language the speak, if the language they input is in the list, the languages I can speak
#I let them know I can speak it as well.
sys.stdout.write("\nType in one language you can speak and see if I can speak it too. \n")

languages = ["Japanese", "English"]

lang = sys.stdin.readline().strip()

if lang in languages:
    sys.stdout.write("Hey, I can speak " +lang+ " too! \n \n")

else:
   sys.stdout.write("I don't know that one. \n \n")



#To be honest, I didn't understand how to utilise the data set we downloaded for IIE 1 so to show
#I understand at least how to add data to a list,
flower = [5.1, 3.5, 1.4, 0.2]

sys.stdout.write("Find a flower, measure it and write in cms with an interger below. e.g. 18.0 or 6.3: ")
userinput = flower.append(float(sys.stdin.readline().strip()))
sys.stdout.write("Thank you, we'll add it to our list. \n")

sys.stdout.write("Type \"flower\" \(Case Sensitive\) to show list. \n")



#add a list of everything the user has enputed. Yet to figure out to get this line to run after user types "flower".
#sys.stdout.write("You are, " +firstname+ " " +surname+ " aged, "+str(value)+ " can speak " +lang+" and picked a flower that is " +str(userinput)+" tall.\n")
#sys.stdin.readline()
