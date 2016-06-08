#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int mutlower(int x, int k);
int mutupper(int x, int k);

int main(int argc, string argv[])
{
    //deal with argc
    if (argc != 2)
    {
        printf("Usage: %s <key>\n", argv[0]);
        return 1;
    }
    //deal with key[]
    string k = (argv[1]);
    int kn = strlen(k);
    int key[kn];
    for(int i = 0; i < kn; i++)
    {
        if islower(k[i])
        {
            key[i] = k[i] - 'a';
        }
        else if isupper(k[i])
        {
            key[i] = k[i] - 'A';
        }
        else
        {
            printf("Keyword must only contain letters A-Z and a-z\n");
            return 1;
        }
    }
    
    //print cipher
    int counter = 0;
    string plaintext = GetString();
    for (int i = 0, n = strlen(plaintext); i < n; i++ )
    {
        if islower(plaintext[i])
        {
            printf("%c", mutlower(plaintext[i], key[counter%kn]));
            counter++;
        }
        else if isupper(plaintext[i])
        {
            printf("%c", mutupper(plaintext[i], key[counter%kn]));
            counter++;
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