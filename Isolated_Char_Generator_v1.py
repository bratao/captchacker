#!coding: utf-8
import sys
sys.path.append("/media/sda4/ecp/Mod1/Pattern Recognition/Project/Code/pycaptcha")

from Captcha.Visual import Text, Backgrounds, Distortions, ImageCaptcha
from Captcha import Words
import random
import os
import ImageFont

"""
        font = ImageFont.truetype(*self.font)
        textSize = font.getsize(self.text)
"""

class MyCaptcha(ImageCaptcha):

    def __init__(self, scale = 35, distortion = (5,5), solution = "9C8G5D"):
        self.distortion = distortion
        self.scale = scale
        self.fontFactory = Text.FontFactory(scale, "califfb/CALIFB.ttf")
        self.solution = solution
        
        font = ImageFont.truetype(*self.fontFactory.pick())
        textSize = font.getsize(self.solution)
        print textSize
        #self.defaultSize = (38, self.distortion[0]+10+self.scale)
        self.defaultSize = (38, 31)
        ImageCaptcha.__init__(self)
        
        
    def getLayers(self):
        #self.addSolution(self.solution)

        textLayer = Text.TextLayer(self.solution,fontFactory = self.fontFactory,alignment = (0.5,0.5))

        return [
            Backgrounds.SolidColor(),
            textLayer,
            Distortions.SineWarp(amplitudeRange = self.distortion)
            ]

DESTINATION_FOLDER = 'Isolated_Char_DB'
DISTORTION_W_MIN = 0
DISTORTION_W_MAX = 10
DISTORTION_H_MIN = 0
DISTORTION_H_MAX = 10
SCALE_MIN = 25
SCALE_MAX = 31

GENERATE_CAPITAL_LETTERS = True
GENERATE_NONCAPTIAL_LETTERS = False
GENERATE_DIGITS = True

elem_to_gen = []

if GENERATE_CAPITAL_LETTERS:
    for i in range(65,91):
        elem_to_gen.append(chr(i))

if GENERATE_DIGITS:
    for i in range(48,58):
        elem_to_gen.append(chr(i))

#elem_to_gen=['A']


if not os.path.isdir(DESTINATION_FOLDER):
    os.mkdir(DESTINATION_FOLDER)

for elem in elem_to_gen:
    if not os.path.isdir(os.path.join(DESTINATION_FOLDER, elem)):
        os.mkdir(os.path.join(DESTINATION_FOLDER, elem))
    for scale in range(SCALE_MIN, SCALE_MAX):
        for distort_w in range(DISTORTION_W_MIN,DISTORTION_W_MAX):
            for distort_h in range(DISTORTION_H_MIN,DISTORTION_H_MAX):
                captcha=MyCaptcha(scale, distortion = (distort_w,distort_h), solution = elem)
                image=captcha.render()
                image.save(DESTINATION_FOLDER+'/'+elem+'/'+elem+'_'+str(scale)+'_'+str(distort_w)+'_'+str(distort_h)+'.bmp')
  
