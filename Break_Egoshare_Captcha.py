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
        print "####################################################################################"
        print "\tLoading model ", chemin
        print "####################################################################################"
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
        str = os.path.join("\ ".join(os.getcwd().split(" ")) ,"Egoshare", "\ ".join('Egoshare Preprocessing'.split(' '))+" "+"\ ".join(file.split(" ")))
        os.system(str)
    
    
    letter1 = Image.open(os.path.join(os.getcwd(), "letter1.bmp")).copy()
    letter1_algo = letter1.point(lambda i: (i/255.))
    
    letter2 = Image.open(os.path.join(os.getcwd(), "letter2.bmp")).copy()
    letter2_algo = letter2.point(lambda i: (i/255.))
    
    letter3 = Image.open(os.path.join(os.getcwd(), "letter3.bmp")).copy()
    letter3_algo = letter3.point(lambda i: (i/255.))
    
    os.remove("letter1.bmp")
    os.remove("letter2.bmp")
    os.remove("letter3.bmp")
    
    if parent:
        w, h = letter1.size
        letter1 = letter1.convert('RGB').resize((parent.zoom*w, parent.zoom*h))
        letter2 = letter2.convert('RGB').resize((parent.zoom*w, parent.zoom*h))
        letter3 = letter3.convert('RGB').resize((parent.zoom*w, parent.zoom*h))

    if parent:
        return beau_captcha, letter1, letter2, letter3, letter1_algo, letter2_algo, letter3_algo
    else:
        return letter1_algo, letter2_algo, letter3_algo


def predict(model, im):
    data = list(im.getdata())
    prediction = model.predict(data)
    probability = model.predict_probability(data)  
    
    if VERBOSE:
        print chr(65+int(prediction)), max(probability[1].values())
        #print probability
    
    return chr(65+int(prediction)), str(max(probability[1].values())), probability[1]
    
    
    
def break_captcha(model, letter1_algo, letter2_algo, letter3_algo, parent=None):
    liste_probas = []
    
    if not TEST:
        prediction1, max_score1, dico1 = predict(model, letter1_algo)
        prediction2, max_score2, dico2 = predict(model, letter2_algo)
        prediction3, max_score3, dico3 = predict(model, letter3_algo)
    else:
        prediction1, max_score1 = "M", "0.21313"
        prediction2, max_score2 = "M", "0.21313"
        prediction3, max_score3 = "M", "0.21313"

    if parent:
        parent.setResults(prediction1, max_score1, prediction2, max_score2, prediction3, max_score3, dico1, dico2, dico3)
    
    return prediction1+prediction2+prediction3




def test_folder(model):
    
    
    pass




#TRACEBACK
import traceback
import sys
def Myexcepthook(type, value, tb):
        lines=traceback.format_exception(type, value, tb)
##        f=open('log.txt', 'a')
##        f.write("\n".join(lines))
##        f.close()
        print "\n".join(lines)
        raw_input()
        sys.exit(0)
sys.excepthook=Myexcepthook


def write(s):
    f=open("Egoshare/Models/Stats.txt", "a")
    f.write(s+"\n")
    f.close()


if __name__ == "__main__":
    MODEL_FOLDER = 'Egoshare/Models'
    MODEL_FILES = ['model_C=1000_KERNEL=2.svm']
    LABELED_CAPTCHAS_FOLDER = 'Egoshare/Labelled Catpchas Test'
    
    try:
        print MODEL_FILE
    except:
        MODEL_FILES = ['model_C=1000_KERNEL=2.svm']
    else:
        MODEL_FILES = [MODEL_FILE]
    
    for file in MODEL_FILES:
        model = load_model(os.path.join(MODEL_FOLDER, file))
        
        nbs = 0
        errors = 0
        for folder, subfolders, files in os.walk(LABELED_CAPTCHAS_FOLDER):
            for file in [file for file in files if file[-4:] == ".jpg"]:
                letter1_algo, letter2_algo, letter3_algo = preprocess_captcha_part(os.path.join(folder, file))
                prediction = break_captcha(model, letter1_algo, letter2_algo, letter3_algo)
                #print "SOLUTION: ", file[:3], "\t",
                #print "PREDICTION: ", prediction, "\t",
                if file[:3] == prediction:
                    #print "SUCCESS"
                    pass
                else:
                    #print "FAILURE"
                    errors += 1
                nbs += 1
        print "\tSuccess rate: ", (1 - (1.*errors/nbs))*100, "%"
        print 
        write(MODEL_FILE+'\t'+str((1 - (1.*errors/nbs))*100)+"%")
