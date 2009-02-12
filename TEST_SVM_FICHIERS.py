from svm import *
import os, sys
import Image

import psyco
psyco.full()

##############################################################################
############################    TRAINING    ##################################
##############################################################################

DESTINATION_FOLDER = 'DBTraining'


labels = []
samples = []


print " CHARGEMENT IMAGES ..."

for folder, subfolders, files in os.walk("DBTraining"):
    for file in [file for file in files if 'bmp' in file]:
        #print file
        im = Image.open(os.path.join(folder, file))

        labels.append(ord(folder[-1])-65)

        samples.append(map(lambda e:e/255., list(im.getdata())))



print " TEST SVM ..."

problem = svm_problem(labels, samples);
size = len(samples)

#param = svm_parameter(C = 10,nr_weight = 2,weight_label = [1,0],weight = [10,1], probability=1)
param = svm_parameter(kernel_type = RBF, C=10, probability = 1)


#kernels : LINEAR, POLY, RBF, and SIGMOID
#types : C_SVC, NU_SVC, ONE_CLASS, EPSILON_SVR, and NU_SVR


model = svm_model(problem,param)
errors = 0
for i in range(size):
    prediction = model.predict(samples[i])
    probability = model.predict_probability
    if (labels[i] != prediction):
        errors = errors + 1
print " kernel %s: error rate = %d / %d" % (param.kernel_type, errors, size)

def predict(model, chemin_image):
    
    if not os.path.isfile(chemin_image):
        print "FICHIER INEXISTANT"
        return

    data = list(Image.open(chemin_image).convert('L').getdata())
    data = map(lambda e:e/255., data)
    
    prediction = model.predict(data)
    probability = model.predict_probability(data)  
    
    #print prediction,
    print probability
    return prediction


def analyze_folder(folder = '.\\DBTest\\A'):
    errors = 0
    nb = 0
    for folder, subfolders, files in os.walk(folder):
        for file in [file for file in files if 'bmp' in file]:
            prediction = predict(model, os.path.join(folder, file))
            if prediction != ord(folder[-1])-65:
                errors += 1
            nb += 1
    print "Errors: %d / %d\n" % (errors, nb)



print "TRAINING"
analyze_folder('.\\DBTraining\\A')
analyze_folder('.\\DBTraining\\B')

print "\nTEST"
analyze_folder('.\\DBTest\\A')
analyze_folder('.\\DBTest\\B')


raw_input()
