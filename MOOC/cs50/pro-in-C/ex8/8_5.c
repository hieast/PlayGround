#include <stdio.h>
float absoluteValue(float x)
{
    if (x < 0)
    x = -x;
    return x;
}

float squareRoot(float x, float epsilon1)
{
    const float epsilon = epsilon1;
    float guess = 1.0;

    while (absoluteValue(guess * guess / x -1) >= epsilon)
        guess = (x / guess + guess) / 2.0;

    return guess;
    }

int main(void)
{
    printf ("squareRoot (2000000000000.0) = %.1f\n", squareRoot(2000000000000.0, 0.1));
    printf ("squareRoot (2000000000000.0) = %.2f\n", squareRoot(2000000000000.0, 0.01));
    printf ("squareRoot (2000000000000.0) = %.3f\n", squareRoot(2000000000000.0, 0.001));
    
    return 0;
}