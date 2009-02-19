#include "cv.h"
#include "cxcore.h"
#include "highgui.h"
#include <iostream>
#include <string>

#if defined (WIN32)
#pragma comment(lib,"cv")
#pragma comment(lib,"cvaux")
#pragma comment(lib,"cxcore")
#pragma comment(lib,"highgui")
#pragma comment(lib,"cvcam")
#endif

using namespace std;

int main(int argc, char *argv[])
{
	string filenameIN;
	if (argc < 2)
		filenameIN = "test.jpg";
	else
		filenameIN = argv[1];

	string filenameOUT = "testOUT.bmp";
	filenameOUT = filenameIN.substr(0,filenameIN.size()-3);
	filenameOUT += "bmp";


    int threshold = 150, maxValue = 255;
    int thresholdType = CV_THRESH_BINARY;

    IplImage *srcImg=0,*gray=0,*grayThresh=0;
	srcImg = cvLoadImage(filenameIN.c_str(),1);

    gray = cvCreateImage( cvSize(srcImg->width, srcImg->height), IPL_DEPTH_8U, 1 );

    cvCvtColor(srcImg, gray, CV_BGR2GRAY );

    grayThresh = cvCloneImage( gray );

    cvThreshold(gray, grayThresh, threshold, maxValue, thresholdType);


    if(!cvSaveImage(filenameOUT.c_str(),grayThresh)){
        cout << "WARNING: Pic can't be saved" <<endl;
        exit(2);

    }

    cout << filenameOUT << " successfully written" << endl;

    cvReleaseImage( &srcImg );
    return 0;

}
