# Visuals Patch (v1.5.4):

# VisualsPatch > Add a loading bar for when certain actions happen

# VisualsPatch > Add a floating + spinning cube to the screen once the user leaves the editor.
# It will loop through an animation for 5 seconds before the app auto closes


# Testing the loading bar + rotating cube for the update
import loadingBar as lb
import rotatingCube as rc
while True:
    x = input("bar or cube? ")
    if x == "bar":
        lb.bar()
        print('\n')
    elif x == "cube":
        rc.cube()
        print('\n')
    else:
        print("Type properly\n")