#include <stdio.h>

int main (void)
{
    int i = 0xffffffff;
    printf ("%x\n", i);
    if ((i >> 4) == i)
        printf ("arithmetic right shift\n");
    else
        printf ("logical right shift\n");
        
    unsigned int j  = 0xffffffff;
    printf ("%x\n", j);
    if ((j >> 4) == j)
        printf ("arithmetic right shift\n");
    else
        printf ("logical right shift\n");
    return 0;
}