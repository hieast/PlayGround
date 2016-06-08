#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf ("Number: ");
    long long int num = GetLongLong();
    int num_length = 0, sum = 0, first = 0, second = 0;
    //printf ("%lli \n", num);
    
    for(int i = 0; num > 0; )
    {
        if(i%2 == 0)
            sum += num%10;
        else
        {
            if (num%10 >= 5)
                sum += (num%10)*2 - 9;
            else
                sum +=  (num%10)*2;
        }
            
        second = first;
        first = num%10;
        num /= 10;
        num_length = ++i;
    }
    //printf ("length: %d, sum: %d , first: %d, second: %d\n", num_length, sum, first, second);
    if (sum%10 == 0)
    {
        if (num_length == 15 && first == 3 && (second == 4 || second == 7))
            printf ("AMEX\n");
        else if (num_length == 16 && first == 5 && (second == 1 || second == 2 
                 || second == 3 || second == 4 || second == 5))
            printf ("MASTERCARD\n");
        else if ( first == 4 && (num_length == 13 || num_length == 16 ))
            printf ("VISA\n");
        else
            printf ("INVALID\n");
        
    }
    else
        printf ("INVALID\n");
    return 0;
}