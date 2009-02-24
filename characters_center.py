import os, sys, time

import psyco
psyco.full()

WIDTH = 20
HEIGHT = 20

TRAINING_FOLDER = "Egoshare/DBTraining-Simulation_based"

for folder, subfolders, files in os.walk(TRAINING_FOLDER):
    
    print folder
        
    if os.name == "nt":
        command = 'centrage.exe "%s" %d %d'%(folder, WIDTH, HEIGHT)
    else:
        #Some Linux stuff :)
        pass
    
    os.system(command)

