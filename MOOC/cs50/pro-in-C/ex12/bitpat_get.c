#include <stdio.h>

int int_size (void)
{
    unsigned int i = ~0;
    int result = 0;
    for (;i != 0; i>>=1)
        result++;
    return result;
}

int bit_test(unsigned int x, int n)
{
    return (x >> (32 - n - 1)) & 1;
}

unsigned int bit_set(unsigned int x, int n)
{
    return (x | (1 << (32 - n - 1)));
}

int arg_size (unsigned int i)
{
    int result = 0;
    for (;i != 0; i>>=1)
        result++;
    return result;
}

unsigned int bitpat_get(unsigned int source, int begin, int len)
{
    unsigned int result = 0;
    for (int i = 0; i < len; i++){
        result <<= 1;
        result += bit_test(source, int_size () - arg_size (source) + begin + i);
    }
    return result;
    
}

int main (void)
{
    printf ("%x \n", bitpat_get(0xe1f4, 11, 3));
    
    return 0;
}