#include <stdio.h>

int main()
{
    float a;
    a = 0;
    while (a <= 100)
    {
        printf("%6.1f degrees F = %6.1f degrees C\n",
            a, (a - 32.0) * 5.0 / 9.0);
        a = a + 10;
    }
    return 0;
}