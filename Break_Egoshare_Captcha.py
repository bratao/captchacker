#!coding: utf-8
from svm import *
import os, sys
import Image, time
import wx

import psyco
psyco.full()

from Preprocess import preprocess_captcha
from Preprocess import load_image

TEST = 0
VERBOSE = 0


def load_model(chemin, parent=None, fichier = ""):
    if not os.path.isfile(chemin):
        print 'The specified model file: \"'+chemin +'\" was not found. Aborting.'
        sys.exit(1)
    else:
        print "Loading model..."
        if parent:
            parent.SetPathLabel("Loading model...")
        model = svm_model(chemin)
        print "Model successfully loaded."
        if parent:
            parent.SetPathLabel(fichier)
            parent.model = model
            parent.model_selected = True
    return model


def preprocess_captcha_part(file, folder=".", parent = None):
    #Fait l'extraction à  partir de la starting position, sur une largeur length, et fait éventuellement du preprocessing.
    
    if parent:
        beau_captcha = Image.open(file)
        w,h = beau_captcha.size
        beau_captcha = beau_captcha.convert('RGB').resize((parent.zoom*w, parent.zoom*h))
    
    if os.name == "nt":
        str = '""'+os.path.join(os.getcwd(), "Egoshare", 'Egoshare.exe" "'+file+'""')
        os.system(str)
    else:
        #Some Linux stuff :)
        pass
    
    letter1 = Image.open(os.path.join(os.getcwd(), "letter1.bmp")).copy()
    letter1_algo = letter1.point(lambda i: (1 - i/255.))
    
    letter2 = Image.open(os.path.join(os.getcwd(), "letter2.bmp")).copy()
    letter2_algo = letter2.point(lambda i: (1 - i/255.))
    
    letter3 = Image.open(os.path.join(os.getcwd(), "letter3.bmp")).copy()
    letter3_algo = letter3.point(lambda i: (1 - i/255.))
    
    os.remove("letter1.bmp")
    os.remove("letter2.bmp")
    os.remove("letter3.bmp")
    
    if parent:
        w, h = letter1.size
        letter1 = letter1.convert('RGB').resize((parent.zoom*w, parent.zoom*h))
        letter2 = letter2.convert('RGB').resize((parent.zoom*w, parent.zoom*h))
        letter3 = letter3.convert('RGB').resize((parent.zoom*w, parent.zoom*h))

    return beau_captcha, letter1, letter2, letter3, letter1_algo, letter2_algo, letter3_algo
    

def predict(model, im):
    data = list(im.getdata())
    prediction = model.predict(data)
    probability = model.predict_probability(data)  
    
    print chr(65+int(prediction)), max(probability[1].values())
    
    if VERBOSE:
        print probability
    
    return chr(65+int(prediction)), str(max(probability[1].values()))
    
    
    
def break_captcha(model, letter1_algo, letter2_algo, letter3_algo, parent=None):
    
    if not parent:
        print """
        ##############################################################################
        ############################    BREAKING CAPTCHA    ################################
        ##############################################################################
        """

    liste_probas = []
    
    if not TEST:
        prediction1, max_score1 = predict(model, letter1_algo)
        prediction2, max_score2 = predict(model, letter2_algo)
        prediction3, max_score3 = predict(model, letter3_algo)
    else:
        prediction1, max_score1 = "M", "0.21313"
        prediction2, max_score2 = "M", "0.21313"
        prediction3, max_score3 = "M", "0.21313"

    if parent:
        parent.setResults(prediction1, max_score1, prediction2, max_score2, prediction3, max_score3)


if __name__ == "__main__":
    MODEL_FILE = "model.svm"
    CAPTCHA_FILE = os.path.join("Captchas", 'Image011.jpg')
    LENGTH_CAPTCHA_PART = 31
    
    if not TEST:
        model = load_model(MODEL_FILE)
    
    captcha, beau_captcha = preprocess_captcha_part(CAPTCHA_FILE)
    break_captcha(model, captcha, size=38)
    raw_input()



