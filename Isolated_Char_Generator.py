#!coding: utf-8
import psyco
psyco.full()

from Captcha.Visual import Text, Backgrounds, Distortions, ImageCaptcha
from Captcha import Words
import random
import os
import ImageFont

import Image

DEFAULT_SIZE = (38, 31)
SEUIL = 200
FONT_DIRECTORY = "/media/sda4/ecp/Mod1/Pattern Recognition/Project/Code/pycaptcha/Captcha/data/fonts/"
GENERATE_TRAINING_SET = True
GENERATE_VALIDATION_SET = True


### CAPTCHA GENERATOR ###

class MyCaptcha(ImageCaptcha):

    def __init__(self, scale = 35, distortion = (5,5), solution = "9C8G5D"):
        self.distortion = distortion
        self.scale = scale
        self.fontFactory = Text.FontFactory(scale, FONT_DIRECTORY+"califfb/califb.ttf")
        self.solution = solution
        
        font = ImageFont.truetype(*self.fontFactory.pick())
        #textSize = font.getsize(self.solution)
        #print textSize
        #self.defaultSize = (38, self.distortion[0]+10+self.scale)
        self.defaultSize = DEFAULT_SIZE
        ImageCaptcha.__init__(self)
        

    def getLayers(self):
        #self.addSolution(self.solution)

        textLayer = Text.TextLayer(self.solution,
                                   fontFactory = self.fontFactory,
                                   alignment = (0.5,0.5))

        return [
            Backgrounds.SolidColor(),
            textLayer,
            Distortions.SineWarp(amplitudeRange = self.distortion)
            ]


### SET GENERATOR ###

def Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER, DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_list):
    if not os.path.isdir(DESTINATION_FOLDER):
        os.mkdir(DESTINATION_FOLDER)
    else:
        for subdir in os.listdir(DESTINATION_FOLDER):
            for file in os.listdir(os.path.join(DESTINATION_FOLDER, subdir)):
                os.remove(os.path.join(DESTINATION_FOLDER, subdir, file))
            os.rmdir(os.path.join(DESTINATION_FOLDER, subdir))
        
    for elem in elem_list:
        if not os.path.isdir(os.path.join(DESTINATION_FOLDER,elem)):
            os.mkdir(os.path.join(DESTINATION_FOLDER,elem))
        for scale in range(SCALE_MIN, SCALE_MAX, STEP):
            for distort_w in range(DISTORTION_W_MIN,DISTORTION_W_MAX, STEP):
                for distort_h in range(DISTORTION_H_MIN,DISTORTION_H_MAX, STEP):
                    captcha=MyCaptcha(scale, distortion = (distort_w,distort_h), solution = elem)
                    image=captcha.render().convert('L')
                    
                    for i in xrange(DEFAULT_SIZE[0]):
                        for j in xrange(DEFAULT_SIZE[1]):
                            val = image.getpixel((i,j))
                            if val < SEUIL:
                                val = 0
                            else:
                                val = 255
                            image.putpixel((i,j), val)
            
                    file = os.path.join(DESTINATION_FOLDER,elem,elem+'_'+str(scale)+'_'+str(distort_w)+'_'+str(distort_h)+'.bmp')
                    image.save(file)
        print elem + " files generated."


### ELEMENT LIST GENERATOR ###

def Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS):
        elem_list = []
        
        if GENERATE_CAPITAL_LETTERS:
            for i in range(65,91):
                elem_list.append(chr(i))
            
        if GENERATE_DIGITS:
            for i in range(48,58):
                elem_list.append(chr(i))
            
        return elem_list


if GENERATE_TRAINING_SET:
    print """
    ##############################################################################
    ##########################   TRAINING    SET   #################################
    ##############################################################################
    """
    
    #GENERATE_CAPITAL_LETTERS = True
    #GENERATE_DIGITS = True
    #elem_list = Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS)
    
    elem_list='3de2mtfr'
    
    DESTINATION_FOLDER = 'DBTraining'
    CLEAN_DESTINATION_FOLDER = True
    DISTORTION_W_MIN = 0
    DISTORTION_W_MAX = 10
    DISTORTION_H_MIN = 0
    DISTORTION_H_MAX = 10
    SCALE_MIN = 25
    SCALE_MAX = 31
    STEP = 1
    Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_list)


if GENERATE_VALIDATION_SET:
    print """
    ##############################################################################
    ###########################      TEST   SET      ################################
    ##############################################################################
    """
    
    #GENERATE_CAPITAL_LETTERS = True
    #GENERATE_DIGITS = True
    #elem_list = Generate_Element_List(GENERATE_CAPITAL_LETTERS, GENERATE_DIGITS)
    
    elem_list='3de2mt'
    
    DESTINATION_FOLDER = 'DBTest'
    CLEAN_DESTINATION_FOLDER = True
    DISTORTION_W_MIN = 0
    DISTORTION_W_MAX = 6
    DISTORTION_H_MIN = 0
    DISTORTION_H_MAX = 10
    SCALE_MIN = 25
    SCALE_MAX = 30
    STEP = 2
    
    Generate_Set(DESTINATION_FOLDER,CLEAN_DESTINATION_FOLDER,DISTORTION_W_MIN,DISTORTION_W_MAX,DISTORTION_H_MIN,DISTORTION_H_MAX,SCALE_MIN,SCALE_MAX,STEP, elem_list)









