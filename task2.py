#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254
Radiusquestion = "What is the radius of the sphere?"
answer = input(Radiusquestion)
x = int(answer)
pI = 3.14

three = 3

fraction = 4/3

volume = (fraction)*(pI)*(x)**three
print(f"volume of sphere: {volume}")
