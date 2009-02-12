#!coding: utf-8
from svm import *
import os, sys
import Image

import psyco
psyco.full()

from Preprocess import preprocess_captcha

VERBOSE = 0
MODEL_FILE = "model.svm"
CAPTCHA_FILE = 'Image011.jpg'
STARTING_POSITION_STEP = 1
LENGTH_CAPTCHA_PART = 31
FOLDER_CAPTCHAS = "Captchas"

if not os.path.isfile(MODEL_FILE):
    print 'The specified model file: \"'+MODEL_FILE +'\" was not found. Aborting.'
    sys.exit(1)
else:
    model = svm_model(MODEL_FILE)
    print "Model successfully loaded."
    

def predict(model, im):
    data = list(im.getdata())
    prediction = model.predict(data)
    probability = model.predict_probability(data)  
    
    print chr(65+int(prediction)),
    if VERBOSE:
        print probability
    
    return prediction



def preprocess_captcha_part(CAPTCHA_FILE):
    #Fait l'extraction à  partir de la starting position, sur une largeur length, et fait éventuellement du preprocessing.
    
    dest = preprocess_captcha(FOLDER_CAPTCHAS, CAPTCHA_FILE)
    
    data = Image.open(dest).convert('L')
    data = data.point(lambda i: i /255.)

    return data



print """
##############################################################################
############################    BREAKING CAPTCHA    ################################
##############################################################################
"""

print "Prediction on subparts:"
print "-----------------------"

captcha = preprocess_captcha_part(CAPTCHA_FILE)
for starting_pos in range(0, 127-31,STARTING_POSITION_STEP):
    preprocessed_captcha_part = captcha.crop((starting_pos, 0, starting_pos+38, 30))
    prediction = predict(model, preprocessed_captcha_part)

