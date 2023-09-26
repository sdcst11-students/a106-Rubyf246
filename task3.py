#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a = "Give me one number, then press enter."
answerF = input(a)
b = "Give me a second number, then press enter."
answerS = input (b)
c = "Give me the last number, then press enter and see the result"
answerT = input (c) 
Fanswer = int(answerF)
Sanswer = int(answerS)
Tanswer = int(answerT)
equation = (Tanswer - Sanswer)/Fanswer
print(f"x: {equation}")


