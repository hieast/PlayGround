#include <stdio.h>
float absoluteValue(float x)
{
    if (x < 0)
    x = -x;
    return x;
}

float squareRoot(float x, float epsilon1)
{
    float epsilon = epsilon1;
    float guess = 1.0;

    while (absoluteValue(guess * guess - x) >= epsilon){
        guess = (x / guess + guess) / 2.0;
        printf ("guess: %f\n", guess);
    }
    
    return guess;
    }

int main(void)
{
    printf ("squareRoot (2.0) = %.3f\n", squareRoot(2.0, 0.1));
    printf ("squareRoot (2.0) = %.3f\n", squareRoot(2.0, 0.001));
    printf ("squareRoot (2.0) = %.3f\n", squareRoot(2.0, 0.00001));
    printf ("%f", 1414213.5 * 1414213.5);
    printf ("squareRoot (2000000000000.0) = %.3f\n", squareRoot(2000000000000.0, 10000000.0));
    return 0;
}