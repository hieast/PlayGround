#include <stdio.h>

int calculateTriangularNumber(int n)
{
    return n*(n+1)/2;
}

int main(void)
{
    int number, triangularNumber;
    
    for (int counter = 1; counter <= 5; counter++)
    {
    
        printf ("What triangular number do you want? ");
        scanf ("%i", &number);
        
        triangularNumber = calculateTriangularNumber(number);
        
        printf ("The %ith triangular number is %i\n",
                number, triangularNumber);
    }        
    return 0;
}