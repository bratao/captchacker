#include "cv.h"
#include "cxcore.h"
#include "highgui.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

#if defined (WIN32)
#pragma comment(lib,"cv")
#pragma comment(lib,"cvaux")
#pragma comment(lib,"cxcore")
#pragma comment(lib,"highgui")
#pragma comment(lib,"cvcam")
#endif

using namespace std;


#define WIDTH 38
#define HEIGHT 31






int main(int argc, char *argv[])
{
	//Noms de fichiers
	string filenameIN;
	if (argc < 2)
		filenameIN = "test.bmp";
	else
		filenameIN = argv[1];


	//Chargement de l'image
	IplImage *srcImg=0, *res=0;
	srcImg = cvLoadImage(filenameIN.c_str(),0);

	res = cvCreateImage( cvSize(WIDTH, HEIGHT), IPL_DEPTH_8U, 1 );
	cvFillImage(res, 255);


	int xmin=WIDTH, xmax=0, ymin=HEIGHT, ymax=0;
	for (int i=0; i<srcImg->width; ++i)
	{
		for (int j=0; j<srcImg->height; ++j)
		{
			if (cvGet2D(srcImg, j, i).val[0] == 0)
			{
				if (i<xmin)
					xmin = i;
				if (i>xmax)
					xmax = i;
				if (j<ymin)
					ymin=j;
				if (j>ymax)
					ymax=j;
			}
		}
	}

	int offsetx = (WIDTH - (xmax-xmin))/2;
	int offsety = (HEIGHT - (ymax-ymin))/2;
	for (int i=0; i<=xmax-xmin; ++i)
	{
		for (int j=0; j<=ymax-ymin; ++j)
		{
			cvSet2D(res, offsety+j, offsetx+i, cvGet2D(srcImg, ymin+j, xmin+i));
		}
	}


	//cout << "xmin: " << xmin << " xmax: " << xmax << endl;
	//cout << "ymin: " << ymin << " ymax: " << ymax << endl;

	cvSaveImage(filenameIN.c_str(), res);

	//system("pause");

	return 0;


}
