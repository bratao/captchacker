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
STARTING_POSITION_STEP = 1


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


def preprocess_captcha_part(file, parent = None):
    #Fait l'extraction à  partir de la starting position, sur une largeur length, et fait éventuellement du preprocessing.
    
    dest = preprocess_captcha(file, None)
    
    data = Image.open(dest)
    data1 = data.point(lambda i: i /255.)
    
    if parent:
        w, h = data.size
        data = data.convert('RGB').resize((parent.zoom*w, parent.zoom*h))

    return data1, data
    
    

def predict(model, im, liste_probas=None):
    data = list(im.getdata())
    prediction = model.predict(data)
    probability = model.predict_probability(data)  
    
    print chr(65+int(prediction)), max(probability[1].values())
    
    if liste_probas is not None:
        liste_probas.append(probability[1])
    
    if VERBOSE:
        print probability
    
    return chr(65+int(prediction)), max(probability[1].values())
    
    
    
def break_captcha(model, captcha, size=38, parent = None, image=None, liste_scores=[], WIDTH=31):
    
    if not parent:
        print """
        ##############################################################################
        ############################    BREAKING CAPTCHA    ################################
        ##############################################################################
        """

    liste_probas = []
    
    w,h = captcha.size
    
    for starting_pos in range(0, w-size,STARTING_POSITION_STEP):
        if parent:
            if not parent.actif:
                return
            
        preprocessed_captcha_part = captcha.crop((starting_pos, 0, starting_pos+size, 31))
        im = Image.new('L', (WIDTH, 31), 1)
        im.paste(preprocessed_captcha_part, ((WIDTH-size)/2, 0))
        preprocessed_captcha_part = im
        
        if not TEST:
            prediction, max_score = predict(model, preprocessed_captcha_part, liste_probas)
        else:
            prediction, max_score = "M", 0.21313

        if parent:
            w, h = preprocessed_captcha_part.size
            preprocessed_captcha_part = preprocessed_captcha_part.point(lambda e : e*255).convert('RGB').resize((parent.zoom*w, parent.zoom*h))
            
            parent.setResult(preprocessed_captcha_part, prediction, int(max_score*10000000)/10000000.)
            parent.SetRGB(starting_pos + WIDTH/2, 31 - int(max_score*h))
            parent.SetGraphImage(image)
            
            time.sleep(0.5)
        else:
            #liste_scores.append((starting_pos + (38-size)/2+1, 0, max_score))
            liste_scores.append((starting_pos + WIDTH - (WIDTH-size)/2, size, max_score))
            
    if parent:
        parent.launchButton.SetLabel("Lancer le calcul")



#TRACEBACK
import traceback
import sys
def Myexcepthook(type, value, tb):
        lines=traceback.format_exception(type, value, tb)
        f=open('log.txt', 'a')
        f.write("\n".join(lines))
        f.close()
sys.excepthook=Myexcepthook



if __name__ == "__main__":
    MODEL_FILE = "Hotmail/Models/model_c=100.svm"
    CAPTCHA_FILE = os.path.join("Hotmail", "Rough Captchas", 'Image011.jpg')
    LENGTH_CAPTCHA_PART = 31
    
    if not TEST:
        model = load_model(MODEL_FILE)
    
    liste_scores = []
    
    captcha, beau_captcha = preprocess_captcha_part(CAPTCHA_FILE)
    for size in range(15, 30, 2):
        print size
        break_captcha(model, captcha, size, None, None, liste_scores)
    
    import pickle
    f=open('scores.pck', 'w')
    pickle.dump(liste_scores, f)
    f.close()
    
    raw_input()



