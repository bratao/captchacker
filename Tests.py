#!coding: utf-8


import sys
sys.path.append("/media/sda4/ecp/Mod1/Pattern Recognition/Project/Code/pycaptcha")

from Captcha.Visual import Text, Backgrounds, Distortions, ImageCaptcha
from Captcha import Words
import random

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
        self.defaultSize = (150, self.distortion[0]+10+self.scale)

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



captcha=MyCaptcha(scale = 35, distortion = (3,5), solution = "9C8G54")
image=captcha.render()
image.show()
image.save('Captcha2.jpg')
