import os
import shutil

LABELLED_CAPTCHAS_FOLDER = "Labelled Catpchas Training"
DEST_FOLDER = "Simulated_digits"

for i in range(10):
    folder = os.path.join(DEST_FOLDER, str(i))
    if not os.path.isdir(folder):
        os.mkdir(folder)

for folder, subfolders, files in os.walk(LABELLED_CAPTCHAS_FOLDER):
    for file in [file for file in files if file[-4:] == ".jpg"]:
        filename = os.path.join(LABELLED_CAPTCHAS_FOLDER, file)
        print file
        
        if os.name == "nt":
            str = '""'+os.path.join(os.getcwd(), 'Egoshare.exe" "'+filename+'""')
            os.system(str)
        else:
            str = os.path.join("\ ".join(os.getcwd().split(" ")), "\ ".join('Egoshare Preprocessing'.split(' '))+" "+"\ ".join(filename.split(" ")))
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



