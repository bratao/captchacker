#!coding: utf-8

from svm import *
import os
import time

CRANGE = [1000]
KERNEL_TYPE = [RBF]


for C in CRANGE:
    for KERNEL in KERNEL_TYPE:
        
        TRAINING_FOLDER = 'Egoshare/DBTraining'
        TRAINING_FOLDER = 'Egoshare/Simulated_digits'
        TEST_FOLDER = 'Egoshare/DBTest'
        VERBOSE = 0
        MODEL_FOLDER = 'Egoshare/Models'
        MODEL_FILE = "model_WITH_CAPTCHA_DATA_C="+str(C)+"_KERNEL="+str(KERNEL)+".svm"
        GENERATE_ANYWAY = 1

        #Génération du modèle
        execfile("Train & Test SVM.py")
        
        #Test du modèle
        execfile("Break_Egoshare_Captcha.py")


raw_input()