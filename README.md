This game is running with pygame. It was created to be part of a project in biology. 
I put in the git the code for the final version, which is the more complex one named "reaction.py", but I also put the easier version, which is not able to manage changes in the window size, during the game, it is named "simple.py". I also provide the application of this game "Reaction Time.exe" but warning if you have an antivirus, maybe you will not be able to put it on your computer, because of security problem, as it is not an official application known by the antivirus. For your information, I did not put anything harmful in it so it should not damage your computer.

Otherwise, if you have a python environment on your computer you can try to create the app by yourself. You need to install pyinstaller on the repo environment and then type the following command in your terminal:
pyinstaller --onefile --icon=appli.ico --name "Reaction Time" reaction.py

This should create several directory in your repo, and the executable file should be in the "dist" directory that has been created.
