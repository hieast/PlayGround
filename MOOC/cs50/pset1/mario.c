#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        printf ("height: ");
        height = GetInt();
    }
    while (height > 23 || height < 0);
    int width = height +1;
    for (height-- ; height >= 0; height-- )
    {
        for (int i = height; i > 0 ; i-- )
            printf (" ");
        for (int i = width - height; i > 0 ; i--)
            printf ("#");
        printf ("\n");
    }
}