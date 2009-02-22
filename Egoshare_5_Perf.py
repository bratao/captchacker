#!coding: utf-8
from Break_Egoshare_Captcha import *

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
