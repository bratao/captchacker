#!coding: utf-8
import os, Image

SEUIL = 180
FOLDER = 'Images'

for folder, subfolders, file_list in os.walk(FOLDER):
    for file in file_list:
        
        if '.jpg' in file.lower():

            print file

            im=Image.open(FOLDER+'/'+file)
            im = im.crop((24, 8, 151, 39)).convert('L')
            
            w = im.size[0]
            h = im.size[1]
            
            for i in xrange(w):
                for j in xrange(h):
                    val = im.getpixel((i,j))
                    if val < SEUIL:
                        val = 0
                    else:
                        val = 255
                    im.putpixel((i,j), val)
            
            
            im.save(FOLDER+'/'+file[:-4]+".bmp")

            print file    
        
        
