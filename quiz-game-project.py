questions = [
   "Which one of the following is not the property of metals:",
   "\nWhat is used for making wires and cables:",
   "\nCopper sulphate is an example of:",
   "\nWhich of the following is NOT a form of energy:",
   "\nfood is a source of:"

]

options = [        
    ["A) shiny", "B) brittle", "C) malleable", "D) sonorous"],
    ["A) iron", "B) copper", "C) tin", "D) brass"],
    ["A) a mixture", "B) an alloy", "C) an element", "D) a compound"],
    ["A) electricity", "B) gravity", "C) sound", "D) light"],
    ["A) kinetic energy", "B) chemical energy", "C) mechanical energy", "D) sound energy"]
]


answers = ["B", "B", "D", "B", "B"]

score = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1, ":", questions[i])
    for option in options[i]:
        print(option)

    user_answer = input("Your Answer (A/B/C/D): ").strip().upper()

    if user_answer == answers[i]:
        print("Right Answer!")
        score += 1
    else:
        print("Wrong Answer. Right Answer is:", answers[i])
        score -= 0.5

#score<0 means negative score
if (score<0):
    score=0
percentage=(score/len(questions))*100
print("\nGame End ! Your score:", score, "/", len(questions))
print("Percentage: ",percentage, "%")
