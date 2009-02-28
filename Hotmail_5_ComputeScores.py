#!coding: utf-8
import Break_Captcha_util
import pickle
import os
import Image

#TRACEBACK
import traceback
import sys
def Myexcepthook(type, value, tb):
        lines=traceback.format_exception(type, value, tb)
        f=open('log.txt', 'a')
        f.write("\n".join(lines))
        f.close()
sys.excepthook=Myexcepthook


MODEL_FILE = "Hotmail/Models/model_31x31.svm"
MODEL_FILE = "Hotmail/Models/model_31x31_3DE2MT_classes.svm"
CAPTCHA_FILE = os.path.join("Hotmail", "Rough Captchas", 'Image011.jpg')


#Chargement du modèle
model = Break_Captcha_util.load_model(MODEL_FILE)

#Liste des scores
liste_scores = []

#Calcul des scores
captcha, beau_captcha = Break_Captcha_util.preprocess_captcha_part(CAPTCHA_FILE)

for size in range(11, 28, 1):
    print size
    for starting_pos in range(0, captcha.size[0] - size):
        preprocessed_captcha_part = captcha.crop((starting_pos, 0, starting_pos+size, 31))
        
        
        #Si parent=None, on enlève le blanc sur les cotés
        miny=100000
        maxy=0
        for i in xrange(size):
            for j in xrange(31):
                if preprocessed_captcha_part.getpixel((i,j)) == 0:
                    if j<miny:
                        miny=j
                    if j>maxy:
                        maxy=j        
        preprocessed_captcha_part = preprocessed_captcha_part.crop((0, miny, size, maxy+1))
        sizei = maxy-miny+1

        im = Image.new('L', (31, 31), 1)
        im.paste(preprocessed_captcha_part, ((31-size)/2, (31-sizei)/2))
##        im1 = im.point(lambda e:e*255)
##        im1.save('temp.bmp')
##        im1.show()
        
        prediction, max_score = Break_Captcha_util.predict(model, im)
        liste_scores.append((starting_pos+size-1, size, max_score, prediction))


f=open('scores.pck', 'w')
pickle.dump(liste_scores, f)
f.close()


