#include "cv.h"
#include "cxcore.h"
#include "highgui.h"
#include "iostream"
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
    /* if(argc<2){
        printf("Usage: main <image-file-name>\n\7");
        exit(0);
    }*/


    string filenameOUT = "testOUT.bmp";

    int threshold = 150, maxValue = 255;
    int thresholdType = CV_THRESH_BINARY;

    IplImage *srcImg=0,*gray=0,*grayThresh=0;
    srcImg = cvLoadImage("test.jpg",1);

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
