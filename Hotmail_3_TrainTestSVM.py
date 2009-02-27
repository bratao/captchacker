#!coding: utf-8

TRAINING_FOLDER = 'Hotmail/DBTraining'
TEST_FOLDER = 'Hotmail/DBTest'
VERBOSE = 0
MODEL_FILE = "model_31x31.svm"
MODEL_FOLDER = "Hotmail/Models"
GENERATE_ANYWAY = 1

C=1000
KERNEL=2

execfile("Train & Test SVM.py")
