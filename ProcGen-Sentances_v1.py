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

axiom = "S"
resultText = axiom
testList = []

for i in range(0, iterations, 1):
    #copy and reset lists
    testList = resultText
    resultText = []

    for rule in testList:
            #check if rule exists and exit otherwise
            if rule in syntaxRules:
                #get options for the current rule
                options = syntaxRules[rule]
                #choose random results to add
                randomRuleNum = random.randint(0, len(options) - 1)
                
                #add results
                for x in options[randomRuleNum]:
                    resultText.append(x)
    
    print(resultText)




file = open("output.txt", "a")
sentance = " ".join(resultText)
file.write(f"[i: {iterations}, seed: {seed}]  {sentance} \n")
file.close
