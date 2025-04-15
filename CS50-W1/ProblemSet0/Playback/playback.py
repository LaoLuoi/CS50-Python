# Defines a function playback
def playback():
    mesage = input("What do you wanna say?: ") # Input
    print(mesage.strip().replace(" ", "...")) # Strip and replace input

playback() # Call function playback
