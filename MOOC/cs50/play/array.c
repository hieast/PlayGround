#include <stdio.h>

int main(void)
{
    int a[5];
    for (int i=0; i<5;a[i++] = 0);
    
    for (int i=0; i<5; i++)
        printf("%i\n", a[i]);
}
