#!coding: utf-8
import psyco
from Isolated_Char_Generator import *

DEFAULT_SIZE = (20, 20)

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


