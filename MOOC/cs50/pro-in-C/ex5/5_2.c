#include <stdio.h>

int main(void)
{
 int n = 10;
 
 printf ("squre of 1 to 10\n\n");
 printf (" n           n^2\n");
 printf ("-----------------\n");
 for (int i = 1; i <= n; i++)
 {
     printf ("%-2i          %i\n", i, i*i);
 }
    
 return 0;
}