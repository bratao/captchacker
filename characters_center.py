import os, sys, time

import psyco
psyco.full()

WIDTH = 20
HEIGHT = 20

folder_to_process = "Egoshare/DBTraining-Simulation_based"

if os.name == "nt":
    command = 'centrage.exe "%s" %d %d'%(folder_to_process, WIDTH, HEIGHT)
elif os.name == "posix":
    command = './Centrage %s %d %d'%(folder_to_process, WIDTH, HEIGHT)
else:
    print "OS non supported"
    sys.exit(0)

os.system(command)
