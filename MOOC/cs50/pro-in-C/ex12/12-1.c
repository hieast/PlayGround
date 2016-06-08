#include <stdio.h>

void swap(int * i1, int * i2)
{
    *i1 ^= *i2;
    *i2 ^= *i1;
    *i1 ^= *i2;
}

void set0(int * x)
{
    *x ^= *x;
}


int main (void)
{
    unsigned int word1 = 077u, word2 = 0150u, word3 = 0210u;
    
    printf ("%o ",word1 & word2);
    printf ("%o ",word1 & word1);
    printf ("%o ",word1 & word2 & word3);
    printf ("%o\n",word1 & 1);
    
    printf ("%o ",word1 | word2);
    printf ("%o ",word1 | word1);
    printf ("%o ",word1 | word2 | word3);
    printf ("%o\n",word1 | 1);
    
    printf ("%o ",word1 ^ word2);
    printf ("%o ",word1 ^ word1);
    printf ("%o ",word1 ^ word2 ^ word3);
    printf ("%o\n",word1 ^ 1);
    
    printf ("%o ",~word2);
    printf ("%o ",~word1);
    printf ("%o \n",~word3);
    
    int i1 = 1, i2 = 2;
    printf ("original %i, %i \n", i1, i2);
    swap(&i1, &i2);
    printf ("swaped %i, %i \n", i1, i2);
    set0(&i1);
    set0(&i2);
    printf ("after set 0 : %i, %i \n", i1, i2);
    return 0;
}