import random

iterations = int(input("how many iterations: "))
seed = input("seed: ")
random.seed(seed)
syntaxRules = {"S"  : [["NP", "VP"]], 
               "VP" : [["V"], 
                       ["TV", "NP"], 
                       ["DTV", "NP", "NP"], 
                       ["SV", "S"], 
                       ["VP", "Adv"], 
                       ["VP", "PP"]], 
               "NP" : [["Det", "N"], 
                       ["PropN"]], 
               "N"  : [["Adj", "N"], 
                       ["N", "PP"]], 
               "PP" : [["P", "NP"]]}

# start with an axom
axiom = "S"

# axom is the first list
newList = axiom

# start on the zeroith iteration
i = 0

while i < iterations:
        # the last list is made the last new list
        lastList = newList

        # the new list is reset
        newList = []

        # ever item in the resultText
        for item in lastList:
                
                # only replace the item if its in the dictionary
                # otherwise dump it to the newList
                if item in syntaxRules:

                        # options in the dictionary for this item
                        options = syntaxRules[item]
                        
                        # random itsm from the choices
                        choice = random.choice(options)

                        # add every part of the choice
                        for newItem in choice:
                                newList.append(newItem)

                else:
                        newList.append(item)


        print(newList)
        
        # increase the iteration
        i += 1

# put the last new list into a file
file = open("output.txt", "a")
sentance = " ".join(newList)
file.write(f"[i: {iterations}, seed: {seed}]  {sentance} \n")
file.close
