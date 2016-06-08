#include <stdio.h>
long int x_to_the_n(int x, int n)
{
    if (n == 0)
        return 1;
    else
        return x * x_to_the_n(x, n-1);
}
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
    int a, b, c;
    double x1, x2;
    
    printf("Enter a, b, c: ");
    scanf("%i%i%i", &a, &b, &c);
    
    if (b * b - 4 * a * c < 0){
        printf("The roots are imaginary numbers\n");
    }
    else{
        x1 = (-b + squareRoot(b * b - 4 * a * c, 0.001)) / (2 * a);
        x2 = (-b - squareRoot(b * b - 4 * a * c, 0.001)) / (2 * a);
        printf ("x1 = %g, x2 = %g \n", x1, x2);
    }
    
    return 0;
    
    
}