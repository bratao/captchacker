#!coding: utf-8

TRAINING_FOLDER = 'Egoshare/DBTraining'
TEST_FOLDER = 'Egoshare/DBTest'
VERBOSE = 0
MODEL_FOLDER = 'Egoshare/Models'
MODEL_FILE = "model.svm"
GENERATE_ANYWAY = 0

execfile("Train & Test SVM.py")

raw_input()