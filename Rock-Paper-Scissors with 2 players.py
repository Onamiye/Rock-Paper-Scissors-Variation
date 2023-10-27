Name1 = str(input("What is your name? : "))
Name2 = str(input("What is the other person's name? : "))
countB = 0
countA = 0
final_countA = 0
final_countB = 0

matches = int(input("Enter number of matches: "))
A, B = 0,0
for match in range(matches):

#example Round1: the play can be "PR". 
#This indicates that person A plays Paper and Person B plays Rock for the round. 
#there can be multiple plays for each round
#example: PR SS SR SS 
  
    rounds = input("Enter plays for match:").split()
    for round in rounds:
        A,B  = round[0], round[1]
        if A == "P" and B == "R":
            countA = countA + 1
        elif A == "R" and B == "P":
            countB = countB + 1
        elif A == "S" and B == "R":
            countB = countB + 1
        elif A == "P" and B == "S":
            countB = countB + 1
        elif A == "R" and B == "S":
            countA = countA + 1
        elif A == "S" and B == "P":
            countA = countA + 1
        elif A == B:
            countA = countA + 0
            countB = countB + 0



    if countB > countA:
        final_countB += 1
    elif countA > countB:
        final_countA +=1
    elif countA == countB:
        countA = countA
        countB = countB

    countA = 0
    countB = 0


if final_countB > final_countA:
    print(f"{Name2} wins. Score: {final_countB}")
elif final_countA > final_countB:
    print(f"{Name1} wins. Score: {final_countA}")
elif final_countA == final_countB:
    print("There is no winner")
