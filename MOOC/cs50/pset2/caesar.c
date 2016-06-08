#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int mutlower(int x, int k);
int mutupper(int x, int k);

int main(int argc, string argv[])
{
    if (argc == 1)
    {
        printf("Usage: %s <key>\n", argv[0]);
        return 1;
    }
    else if (argc > 2)
    {
        return 1;
    }
    
    int k = (atoi(argv[1]))%26;
    string plaintext = GetString();
    for (int i = 0, n = strlen(plaintext); i < n; i++ )
    {
        if islower(plaintext[i])
        {
            printf("%c", mutlower(plaintext[i], k));
        }
        else if isupper(plaintext[i])
        {
            printf("%c", mutupper(plaintext[i], k));
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}

int mutlower(int x, int k)
{
    if (x+k < 'a'+25)
    {
        return x+k;
    }
    else
    {
        return x+k-26;
    }
}

int mutupper(int x, int k)
{
    if (x+k < 'A'+25)
    {
        return x+k;
    }
    else
    {
        return x+k-26;
    }
    
}