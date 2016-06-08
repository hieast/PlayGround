#include <stdio.h>
#include <cs50.h>

int main(int argc, char *argv[])//(int argc, string argv[])
{
    printf("%d\n",argc);
    for (int x=0; x<argc; x++)
        printf("%s\n",argv[x]);
    return 0;
}