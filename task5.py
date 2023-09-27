#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.


a = "Give me the volume of the sphere then press enter and see the radius."
answerF = input(a)
Fanswer = float(answerF)
pI = 3.14
equation = (3* Fanswer/ (4* pI))** 1.0/3

print (f"Radius: {equation}")
