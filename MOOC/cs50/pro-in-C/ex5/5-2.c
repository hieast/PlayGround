/* Program to calculate the 200th triangular number
   Introduction of the for statement */

#include <stdio.h>

int main(void)
{
    int n, triangularNumber;
    
    triangularNumber = 0;
    
    for (n = 1; n < 201; n++)
    {
        triangularNumber += n;
    }
    
    printf ("The eighth triangular number is %i\n",
            triangularNumber);
            
    return 0;
}