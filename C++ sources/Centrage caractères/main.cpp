#include "cv.h"
#include "cxcore.h"
#include "highgui.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

#include <iostream>
#include "windows.h"
#include "stdio.h"
#include "dos.h" 
#include <sstream>

#include <cstdlib>
#include <conio.h>



#if defined (WIN32)
#pragma comment(lib,"cv")
#pragma comment(lib,"cvaux")
#pragma comment(lib,"cxcore")
#pragma comment(lib,"highgui")
#pragma comment(lib,"cvcam")
#endif

using namespace std;



string narrow( wstring& str )
{
	ostringstream stm ;
	const ctype<char>& ctfacet =
		use_facet< ctype<char> >( stm.getloc() ) ;
	for( size_t i=0 ; i<str.size() ; ++i )
		stm << ctfacet.narrow( str[i], 0 ) ;
	return stm.str() ;
}




void process_file(string filenameIN, int WIDTH, int HEIGHT)
{
	//cout << "processing file: " << filenameIN << endl;
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
			if ((offsety+j>0) && (offsety+j<res->height) && (offsetx+i>0) && (offsetx+i<res->width))
				cvSet2D(res, offsety+j, offsetx+i, cvGet2D(srcImg, ymin+j, xmin+i));
		}
	}

	cvSaveImage(filenameIN.c_str(), res);

}







int main(int argc, char *argv[])
{
	//Noms de fichiers
	string folder;

	//cout << "ARGC: " << argc << endl;

	int WIDTH;
	int HEIGHT;

	if (argc < 2)
	{
		folder = "*";
		WIDTH = 38;
		HEIGHT = 31;
	}
	else
	{
		folder = argv[1];
		//cout << "filename IN " << folder << endl;

		WIDTH = atoi(argv[2]);
		//cout << "WIDTH " << WIDTH << endl;

		HEIGHT = atoi(argv[3]);
		//cout << "HEIGHT " << HEIGHT << endl;
	}


	string expression_bmp = folder + "\\*.bmp";
	std::vector<std::wstring> SongsLoaded;

	//InitFunction
	WIN32_FIND_DATA findFileData;



	char *expr = (char *) expression_bmp.c_str();
	wchar_t *lpfile = new wchar_t[200];
	mbstowcs(lpfile, expr, strlen(expr));

	//cout << "sizeof: " << sizeof(expr) << endl;
	//cout << "EXPRESSION_BMP CHAR*: " << expr << endl;
	//wcout << "EXPRESSION_BMP: " << lpfile << endl;

	HANDLE hFind = FindFirstFile(lpfile, &findFileData);

	if(hFind  == INVALID_HANDLE_VALUE)
	{
		//cout << "Could Not Find Any file in folder!" << endl;
		//system("pause");
		return 1;
	}

	SongsLoaded.push_back(findFileData.cFileName);

	while(FindNextFile(hFind, &findFileData))
	{
		SongsLoaded.push_back(findFileData.cFileName);
		//wcout << findFileData.cFileName << endl;
	}

	FindClose(hFind);

	for (int i=0; i<SongsLoaded.size(); ++i)
	{
		//wcout << "Traitement: " << SongsLoaded[i] << endl;

		string filename = narrow(SongsLoaded[i]);
		filename = folder + "\\" + filename;

		process_file(filename, WIDTH, HEIGHT);

		//getchar();

	}
	//cout << endl;






	//system("pause");

	return 0;


}




