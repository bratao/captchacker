import os

MODEL_FILE = "Egoshare/Models/model_WITH_CAPTCHA_DATA_C=1000_KERNEL=1.svm"

from Egoshare_1_GetCaptchas import save_image
from Break_Egoshare_Captcha import load_model, preprocess_captcha_part, break_captcha

model = load_model(MODEL_FILE)
print

for i in range(100):
    file = save_image(path = "Egoshare/Rough Captchas/0")
    
    letter1_algo, letter2_algo, letter3_algo = preprocess_captcha_part(file)
    prediction = break_captcha(model, letter1_algo, letter2_algo, letter3_algo)

    new_filename = file[:-1]+prediction+".jpg"
    while os.path.isfile(new_filename):
        new_filename = new_filename[:-4]+"_"+new_filename[-4:]
        print "Changement de nom: ", new_filename

    os.rename(file, new_filename)
    print new_filename
    
raw_input()