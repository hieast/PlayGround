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

int bitpat_search (source, pattern, n)
{
    int i, int_len = int_size();
    int pattern_len = arg_size (pattern);
    int source_len = arg_size (source);
    int is_find = 1;

    for (i = 0 ; i < int_len - pattern_len + 1; i++)
    {
        for (int j = 0; j < pattern_len; j++){

            if (bit_test(source,int_len - source_len + i + j) != bit_test(pattern, int_len - pattern_len + j)){
                is_find = 0;
                break;
            }
                
        }
        if (is_find == 1){
            return i;
        }
        else
            is_find = 1;

    }
    return -1;
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

void bitpat_set(unsigned int *target, unsigned int pattern,int begin,int len)
{
    for (int i = 0; i < len; i++)
    {
        if (bit_test(pattern, int_size () - len + i) == 1)
            *target = *target | (1 << (32 - begin - i - 1));
        else
            *target = *target & (~0 ^ (1 << (32 - begin - i - 1)));
    }
    
    
}

int main (void)
{   unsigned int target = ~0;
    printf ("%x\n", target);
    bitpat_set(&target, 0xbcd,8,20);
    printf ("%x\n", target);
    return 0;
}