#include <stdio.h>

int main(void)
{
    struct rec
    {
        int a,b;
        float c,d;
    } ;
    typedef struct rec data;
    data x;
    x.a = 1;
    x.b = 2;
    x.c = 73.0;
    x.d = 4.0;
    printf ("%c\n", (char) x.c);
    
}