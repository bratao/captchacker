import os, sys, time

import psyco
psyco.full()

WIDTH = 20
HEIGHT = 20

TRAINING_FOLDER = "Egoshare/DBTraining-Simulation_based"

for folder, subfolders, files in os.walk(TRAINING_FOLDER):
    loaded = False
    for file in [file for file in files if 'bmp' in file]:
        if not loaded:
            print "folder", folder, "loaded"
            loaded = True
        
        print file
        
        if os.name == "nt":
            filename = os.path.join(os.getcwd(), folder, file)
            command = '""'+os.path.join(os.getcwd(), 'centrage.exe" "'+filename+'" '+str(WIDTH)+' '+str(HEIGHT)+'"')
        else:
            #Some Linux stuff :)
            pass
        
        os.system(command)



        
