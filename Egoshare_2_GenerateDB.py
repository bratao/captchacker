#!coding: utf-8
import psyco
from Isolated_Char_Generator import *

DEFAULT_SIZE = (20, 20)
SEUIL = 200

GENERATE_TRAINING_SET = True
GENERATE_VALIDATION_SET = True

FONTS = ["Fonts/califb.ttf", "Fonts/vera.ttf"]


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
    DISTORTION_W_MAX = 3
    DISTORTION_H_MIN = 0
    DISTORTION_H_MAX = 3
    SCALE_MIN = 15
    SCALE_MAX = 20
    STEP = 1
    ALIGN_RANGEY = [0.5]
    ALIGN_RANGEX = [0.5]
    ROTATIONS = [3, 7, 11, 15, 19, 23, 27]
    Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,
                 DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_to_gen, FONTS, ALIGN_RANGEX, ALIGN_RANGEY, DEFAULT_SIZE, SEUIL, ROTATIONS)


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
    ALIGN_RANGEY = [0.5]
    ALIGN_RANGEX = [0.5]
    ROTATIONS = [3, 7, 11, 15, 19, 23, 27]
    Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,
                 DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_to_gen, FONTS, ALIGN_RANGEX, ALIGN_RANGEY, DEFAULT_SIZE, SEUIL, ROTATIONS)


