#include <stdio.h>

int bit_test(unsigned int x, int n)
{
    return (x >> (32 - n - 1)) & 1;
}

unsigned int bit_set(unsigned int x, int n)
{
    return (x | (1 << (32 - n - 1)));
}

int main (void)
{
    printf ("bit_test: %i\n", bit_test(0xaaaaaaaa, 1));
    printf ("bit_test: %i\n", bit_test(0xaaaaaaaa, 2));
    printf ("bit_test: %i\n", bit_test(0xaaaaaaaa, 3));
    printf ("bit_test: %i\n", bit_test(0xaaaaaaaa, 4));
    printf ("bit_test: %i\n", bit_test(0xaaaaaaaa, 5));
    printf ("bit_test: %i\n", bit_test(0xaaaaaaaa, 6));
    
    printf ("bit_set: %x\n", bit_set(0x00000000, 0));
    printf ("bit_set: %x\n", bit_set(0x00000000, 1));
    printf ("bit_set: %x\n", bit_set(0x00000000, 2));
    printf ("bit_set: %x\n", bit_set(0x00000000, 3));
    printf ("bit_set: %x\n", bit_set(0x00000000, 4));
    printf ("bit_set: %x\n", bit_set(0x00000000, 5));
    printf ("bit_set: %x\n", bit_set(0x00000000, 6));
    printf ("bit_set: %x\n", bit_set(0x00000000, 7));
    

    
    
    
    return 0;
}