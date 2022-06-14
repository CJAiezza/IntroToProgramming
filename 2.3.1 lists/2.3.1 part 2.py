import sys

countries = {"Italy": "unsafe", "United Kingdom": "safe", "France": "safe", "China": "unsafe", "Canada": "safe"}
pasttimes = ["playing the guitar", "driving", "eating pizza", "using a computer", "watching Star Wars"]


for dickface, status in countries.copy().items():
    if status == "unsafe":
        del countries[dickface]
  
