// Program to illustrate the %s scanf format characters

#include <stdio.h>

int main (void)
{
    char s1[81], s2[81], s3[81];
    
    printf ("Enter text:\n");
    
    scanf ("%80s%80s%80s", s1, s2, s3);
    
    printf ("\ns1= %s\ns2 = %s\ns3 = %s\n", s1, s2, s3);
    printf ("\aSYSTEM SHUT DOWN IN 5 MINUTES!!\n");
    
    return 0;
}