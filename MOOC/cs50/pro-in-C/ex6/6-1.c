// Program to calculate the absolute value of an integer
#include <stdio.h>

int main (void)
{
    float number;
    
    printf ("Type in your number: ");
    scanf ("%g", &number);
    
    if (number < 0)
        number = -number;
    
    printf ("The absolute value is %g\n", number);
    
    return 0;
}