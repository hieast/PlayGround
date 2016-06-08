#include <stdio.h>

#define IS_LOWER_CASE(x) (((x) >='a') && ((x) <= 'z'))
#define TO_UPPER(x) (IS_LOWER_CASE(x)?(x) - 'a' + 'A':(x))
#define IS_UPPER_CASE(x) (((x) >='A') && ((x) <= 'Z'))
#define IS_ALPHABETIC(x) IS_LOWER_CASE(x) | IS_UPPER_CASE(x)
#define IS_DIGIT(x) ((x) >= '0' && (x) <= '9')
#define IS_SPECIAL(x) (!(IS_ALPHABETIC(x) | IS_DIGIT(x)))

int main (void)
{
    char a = 'a', b = 'B', c = '1', d = '\n';
    printf("%i, %i, %i, %i\n",
           IS_UPPER_CASE(a), 
           IS_ALPHABETIC(a), 
           IS_DIGIT(a), 
           IS_SPECIAL(a));
    printf("%i, %i, %i, %i\n",
           IS_UPPER_CASE(b), 
           IS_ALPHABETIC(b), 
           IS_DIGIT(b), 
           IS_SPECIAL(b));
    printf("%i, %i, %i, %i\n",
           IS_UPPER_CASE(c), 
           IS_ALPHABETIC(c), 
           IS_DIGIT(c), 
           IS_SPECIAL(c));
    printf("%i, %i, %i, %i\n",
           IS_UPPER_CASE(d), 
           IS_ALPHABETIC(d), 
           IS_DIGIT(d), 
           IS_SPECIAL(d));
           
    return 0;
    
}
