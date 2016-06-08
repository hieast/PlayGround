#include <stdio.h>
double absoluteValue(double x)
{
    if (x < 0)
    x = -x;
    return x;
}

double squareRoot(double x, double epsilon1)
{
    const double epsilon = epsilon1;
    double guess = 1.0;

    while (absoluteValue(guess * guess / x -1) >= epsilon)
        guess = (x / guess + guess) / 2.0;

    return guess;
    }

int main(void)
{
    printf ("squareRoot (20.0) = %g\n", squareRoot(20.0, 0.00001));
    printf ("squareRoot (200.0) = %g\n", squareRoot(200.0, 0.00001));
    printf ("squareRoot (20000.0) = %g\n", squareRoot(20000.0, 0.00001));
    
    return 0;
}