#!coding: utf-8
import psyco
from Isolated_Char_Generator import *
import shutil

DEFAULT_SIZE = (20, 20)


CAPTCHA_BASED = True
FONT_BASED = False


if FONT_BASED:
    GENERATE_TRAINING_SET = True
    GENERATE_VALIDATION_SET = True


    if GENERATE_TRAINING_SET:
        print """
        ##############################################################################
        #########################   TRAINING    SET   ################################
        ##############################################################################
        """
        
        GENERATE_CAPITAL_LETTERS = False
        GENERATE_DIGITS = True
        elem_to_gen = Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS)
        

        DESTINATION_FOLDER = 'Egoshare/DBTraining'
        CLEAN_DESTINATION_FOLDER = True
        DISTORTION_W_MIN = 0
        DISTORTION_W_MAX = 1
        DISTORTION_H_MIN = 0
        DISTORTION_H_MAX = 1
        SCALE_MIN = 17
        SCALE_MAX = 22
        STEP = 1
        ALIGN_RANGEY = [0.7]
        ALIGN_RANGEX = [0.5]
        SEUIL_RANGE = [160, 180, 200]
        ROTATIONS = [2, 4, 6, 9, 13, 17, 20, 22, 25, 27]
        FONTS = [("Fonts/comic.ttf", (140, 160)),
                 ("Fonts/vera.ttf", (160, 180)),
                 ("Fonts/califb.ttf", (160, 180))]
        Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,
                     DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_to_gen, FONTS, ALIGN_RANGEX, ALIGN_RANGEY, DEFAULT_SIZE, ROTATIONS)


    if GENERATE_VALIDATION_SET:
        print """
        ##############################################################################
        ###########################   TEST   SET      ################################
        ##############################################################################
        """
        
        GENERATE_CAPITAL_LETTERS = False
        GENERATE_DIGITS = True
        elem_to_gen = Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS)

        DESTINATION_FOLDER = 'Egoshare/DBTest'
        CLEAN_DESTINATION_FOLDER = True
        DISTORTION_W_MIN = 0
        DISTORTION_W_MAX = 2
        DISTORTION_H_MIN = 0
        DISTORTION_H_MAX = 2
        SCALE_MIN = 15
        SCALE_MAX = 20
        STEP = 2
        ALIGN_RANGEY = [0.7, 1]
        ALIGN_RANGEX = [0.5]
        ROTATIONS = [2, 9, 13, 22]
        FONTS = [("Fonts/comic.ttf", (140, 160)),
                 ("Fonts/vera.ttf", (160, 180)),
                 ("Fonts/califb.ttf", (160, 180))]
        Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,
                     DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_to_gen, FONTS, ALIGN_RANGEX, ALIGN_RANGEY, DEFAULT_SIZE, ROTATIONS)


if CAPTCHA_BASED:
    LABELLED_CAPTCHAS_TRAINING_FOLDER = "Egoshare/Labelled Catpchas Training"
    DEST_FOLDER = "Egoshare/DBTraining-Simulation_based"

    #Création du dossier de destination
    if not os.path.isdir(DEST_FOLDER):
        os.mkdir(DEST_FOLDER)
        
    #suppression des anciens fichiers
    print "Removing older files..."
    for subdir in os.listdir(DEST_FOLDER):
        if subdir[0] != ".": # to prevent removal of .svn folders !
            for file in os.listdir(os.path.join(DEST_FOLDER, subdir)):
                os.remove(os.path.join(DEST_FOLDER, subdir, file))
            os.rmdir(os.path.join(DEST_FOLDER, subdir))
    print "Done..."
            
    #Création des sous-dossiers
    for i in range(10):
        folder = os.path.join(DEST_FOLDER, str(i))
        if not os.path.isdir(folder):
            os.mkdir(folder)

    #Remplissage des sous-dossiers
    for folder, subfolders, files in os.walk(LABELLED_CAPTCHAS_TRAINING_FOLDER):
        for file in [file for file in files if file[-4:] == ".jpg"]:
            filename = os.path.join(LABELLED_CAPTCHAS_TRAINING_FOLDER, file)
            print file
            
            if os.name == "nt":
                str = '""'+os.path.join(os.getcwd(), "Egoshare", 'Egoshare.exe" "'+filename+'""')
                os.system(str)
            else:
                str = os.path.join("\ ".join(os.getcwd().split(" ")) ,"Egoshare", "\ ".join('Egoshare Preprocessing'.split(' '))+" "+"\ ".join(filename.split(" ")))
                os.system(str)
            
            name1 = file[:-4]+"number_1.bmp"
            name2 = file[:-4]+"number_2.bmp"
            name3 = file[:-4]+"number_3.bmp"
            
            os.rename("letter1.bmp", name1)
            os.rename("letter2.bmp", name2)
            os.rename("letter3.bmp", name3)
            
            shutil.move(name1, os.path.join(DEST_FOLDER, file[0]))
            shutil.move(name2, os.path.join(DEST_FOLDER, file[1]))
            shutil.move(name3, os.path.join(DEST_FOLDER, file[2]))




