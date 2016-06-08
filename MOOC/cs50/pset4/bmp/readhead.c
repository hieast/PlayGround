#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"
#define PRINT(x) printf (#x ":%i\n", x);


int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./readhead bmp_file\n");
        return 1;
    }
    
        // remember filenames
    char* infile = argv[1];

    // open input file 
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }
    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    
    PRINT(bf.bfType)
    PRINT(bf.bfSize)
    PRINT(bf.bfReserved1)
    PRINT(bf.bfReserved2)
    PRINT(bf.bfOffBits)
    PRINT(bi.biSize)
    PRINT(bi.biWidth)
    PRINT(bi.biHeight)
    PRINT(bi.biPlanes)
    PRINT(bi.biBitCount)
    PRINT(bi.biCompression)
    PRINT(bi.biSizeImage)
    PRINT(bi.biXPelsPerMeter)
    PRINT(bi.biYPelsPerMeter)
    PRINT(bi.biClrUsed)
    PRINT(bi.biClrImportant)
    /*
typedef struct 
{ 
    WORD   bfType; 
    DWORD  bfSize; 
    WORD   bfReserved1; 
    WORD   bfReserved2; 
    DWORD  bfOffBits; 
} __attribute__((__packed__)) 
BITMAPFILEHEADER; 
typedef struct
{
    DWORD  biSize; 
    LONG   biWidth; 
    LONG   biHeight; 
    WORD   biPlanes; 
    WORD   biBitCount; 
    DWORD  biCompression; 
    DWORD  biSizeImage; 
    LONG   biXPelsPerMeter; 
    LONG   biYPelsPerMeter; 
    DWORD  biClrUsed; 
    DWORD  biClrImportant; 
} __attribute__((__packed__))
BITMAPINFOHEADER; 
*/
}