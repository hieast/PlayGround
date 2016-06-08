/**
 * recover.c
 *
 * Computer Science 50
 * Problem Set 4
 *
 * Recovers JPEGs from a forensic image.
 */
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#define BLOCK 512

typedef uint8_t  BYTE;
typedef uint32_t DWORD;
typedef int32_t  LONG;
typedef uint16_t WORD;


int main(void)//int argc, char* argv[]
{
    /*
    if (argc != 2)
    {
        printf ("usage:./recover file\n");
        return 1;
    }
    */
    //char *fileName = argv[1];
    char *fileName = "card.raw";
    FILE* file = fopen(fileName, "r");
    if (file == NULL)
    {
        printf ("can't open file\n");
        return 2;
    }

    bool find = false;
    int counter = 0;
    uint32_t head = 0;
    char title[9];
    sprintf(title, "%03i.jpg", counter++);
    FILE* img = fopen(title, "w");
    void *temp = malloc(BLOCK);
    while (fread(&head, sizeof(DWORD), 1, file))
    {
        //read 512 bytes into temp
        BYTE byte4 = head >> 24;
        BYTE byte3 = head << 8 >> 24;
        BYTE byte2 = head << 16 >> 24;
        BYTE byte1 = head << 24 >> 24;
        fseek(file, - sizeof(DWORD), SEEK_CUR);
        fread(temp, BLOCK, 1, file);


        //start of a new jpg?
        if ((byte1 == 0xff) && (byte2 == 0xd8) && (byte3 == 0xff) && (byte4>>4 == 0x0e))
        {
            if(find == false)
            {
                find = true;
                fwrite(temp, BLOCK, 1, img);
            }
            else
            {
                fclose(img);
                sprintf(title, "%03i.jpg", counter++);
                img = fopen(title, "a");
                fwrite(temp, BLOCK, 1, img);
            }
        }
        else if(find == true)
        {
            fwrite(temp, BLOCK, 1, img);
        }

    }
    fclose(file);
    free(temp);
    fclose(img);
    
    //printf ("find %i imgs!\n", counter);
    return 0;
    

}

//ffd8ffe*