# Getting started #

## Simple test: Egoshare GUI ##
As we have already downloaded some captchas, and build some SVM models, you can simply run the program:

  * `Egoshare_4_GUI.py`

Once you have launched the GUI, you should see something similar to this:

http://captchacker.googlecode.com/files/GUI%20Screenshot.JPG

You select a captcha, a model, and see if it breaks the captcha.

### Requirements ###

Here is what you need to be able to do this test:
  * Python 2.5+
  * [PIL (Python Image Library)](http://www.pythonware.com/products/pil/) installed
  * OpenCV 1 (make sure the dlls path is in your environment variable path)
  * [LibSVM](http://www.csie.ntu.edu.tw/~cjlin/libsvm/) Python wrapper (not tested with latest version)
If the line "model = svm\_model(chemin)" fails, try replacing it with "model = svm\_load\_model(chemin)"


## How to get captchas and train models myself ? ##

To continue with the Egoshare example, if you want to do the whole stuff yourself, it is fairly simple. Indeed, all you have to do is running the files `Egoshare_n_*.py`, namely:

  * `Egoshare_1_GetCaptchas.py`
  * `Egoshare_1_bis_GetLabelledCaptchas.py`
  * `Egoshare_2_GenerateDB.py`
  * `Egoshare_3_TrainTestSVM.py`
  * `Egoshare_4_GUI.py`
  * `Egoshare_5_TestPerf.py`

## What about other captchas? ##

The principle remain the same, for Hotmail, you have to run the `Hotmail_n_*.py` files:
  * `Hotmail_1_GetCaptchas.py`
  * `Hotmail_2_GenerateDB.py`
  * `Hotmail_3_TrainTestSVM.py`
  * `Hotmail_4_GUI.py`
  * `Hotmail_5_ComputeScores.py`

Once more, you can just run `Hotmail_4_GUI.py` if you want to do a simple test.

## And what if I want/need to recompile the C++ sources? ##

The C++ sources have been compiled on Windows and Ubuntu, on i386 32bits architectures, and the binaries have been placed in the root directory.

Most users do **not** have to do this, however if you need/want to recompile these sources, here is what you need:

  * A C++ compiler
  * the C++ [OpenCV1 library](http://sourceforge.net/projects/opencvlibrary/) (do not forget the link options to be able to compile).