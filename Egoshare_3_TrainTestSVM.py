#!coding: utf-8

from svm import *
import os
import time


GENERATE_CAPTCHA_BASED_MODELS = True
GENERATE_SIMULATION_BASED_MODELS = False
VERBOSE = 0
MODEL_FOLDER = 'Egoshare/Models'


if GENERATE_CAPTCHA_BASED_MODELS:
    CRANGE = [1000]
    KERNEL_TYPE = [RBF, POLY]
    TRAINING_FOLDER = 'Egoshare/DBTraining-Captcha_based'
    TEST_FOLDER = 'Egoshare/DBTest-Captcha_based'
    GENERATE_ANYWAY = 1

    for C in CRANGE:
        for KERNEL in KERNEL_TYPE:
            MODEL_FILE = "captcha_based_TR=1896_TEST=714_C="+str(C)+"_KERNEL="+str(KERNEL)+".svm"
            #Génération du modèle
            execfile("Train & Test SVM.py")
            #Test du modèle
            execfile("Egoshare_5_Perf.py")
            

if GENERATE_SIMULATION_BASED_MODELS:
    CRANGE = [1000]
    KERNEL_TYPE = [RBF, POLY]
    TRAINING_FOLDER = 'Egoshare/DBTraining-Simulation_based'
    TEST_FOLDER = 'Egoshare/DBTest-Simulation_based'
    GENERATE_ANYWAY = 1

    for C in CRANGE:
        for KERNEL in KERNEL_TYPE:
            MODEL_FILE = "simulation_based_TR=687_TEST=143_C="+str(C)+"_KERNEL="+str(KERNEL)+".svm"
            #Génération du modèle
            execfile("Train & Test SVM.py")

raw_input()
