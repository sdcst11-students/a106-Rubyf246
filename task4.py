#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

a = "Give me the height number, then press enter."
answerF = input(a)
b = "Give me the radius number, then press enter and see the result."
answerS = input (b)
Fanswer = float(answerF)
Sanswer = float(answerS)
equation = (Fanswer**2) + (Sanswer**2)
slant = equation**(1/2)
pI = 3.14
sequation = pI * Sanswer**2 + pI * Sanswer * slant
print (f"SA: {sequation}")