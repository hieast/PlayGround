#include <stdio.h>

#define YES 1
#define NO 0
#define IS_LOWER_CASE(x) (((x) >='a') && ((x) <= 'z'))
#define TO_UPPER(x) (IS_LOWER_CASE(x)?(x) - 'a' + 'A':(x))
#define debugPrintf(...) printf ("DEBUG:" __VA_ARGS__);

int isEven(int number)
{
    int answer;
    if ( number % 2 == 0 )
        answer = YES;
    else
        answer = NO;
    return answer;
}

int main (void)
{
    if (isEven(17) == YES)
        printf ("yes ");
    else
        printf ("no ");
    if(isEven(20) == YES)
        printf ("yes\n");
    else
        printf ("no\n");
    printf ("%c\n", TO_UPPER('b'));
    debugPrintf("x" "y" "z%i\n", 10)
    return 0;
}