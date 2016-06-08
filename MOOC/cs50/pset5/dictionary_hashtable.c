/**
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#include "dictionary.h"
#define SIZE 100000
//#define DEBUG

int num = 0;
struct node
{
    char *value;
    struct node *next;
};
struct node *hashtable[SIZE];

void print_string(char *str)
{
    char c = *str++;
    while (c)
    {
        printf("%c", c);
        c = *str++;
    }
    printf ("->");
}

void print_chain(struct node *root)
{
    if (root != NULL)
    {
        print_string(root->value);
        print_chain(root->next);
    }
}

void print_hash(void)
{
    for(int i = 0; i < SIZE; i++)
    {
        if (hashtable[i] != NULL)
            {
            printf("hashtable[%i]:",i);
            print_chain(hashtable[i]);
            printf("\n");
            }
    }
}

unsigned long hash(const char *str)
    {
        unsigned long hash = 5381;
        int c = *str++;
        while (c)
        {
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
            c = *str++;
        }
        return hash;
    }

bool compare_str(const char *str1, const char *str2)
{
    int i = 0;
    while ((*(str1 + i) == *(str2 + i)) && (*(str1 + i) != '\0'))
    {
        i++;
    }
    return (*(str1 + i) == *(str2 + i));
}



bool search(struct node *root, const char *str)
{
    #ifdef DEBUG
    printf ("-> %lu ", (unsigned long )root);
    #endif
    if (root == NULL)
        return false;
    else 
        return (compare_str(root->value, str)||(search(root->next, str)));
}

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char* word)
{
    char temp[LENGTH+1];
    int i = 0;
    while(word[i]){
        temp[i] = tolower(word[i]);
        i++;
    }
    temp[i] = '\0';
    
    #ifdef DEBUG
    printf ("hash(temp) \%% SIZE: %lu\n", hash(temp) % SIZE);
    print_chain(hashtable[hash(temp) % SIZE]);
    #endif
    
    
    return search(hashtable[hash(temp) % SIZE], temp);
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    FILE *file = fopen(dictionary, "r");
    char c;
    int index = 0;
    char word[LENGTH+1];
    while ( (c = fgetc(file)) != EOF)
    {
        if (c != '\n')
        {
            word[index] = c;
            index++;
        }
        else
        {
            char *temp = malloc((index + 1) * sizeof(char));
            for(int i = 0; i < index; i++)
                temp[i] = word[i];
            temp[index] = '\0';
            
            unsigned long target = hash(temp) % SIZE;
            
            #ifdef DEBUG
            printf ("hashtable[%lu]:\n", target);
            print_chain(hashtable[target]);
            #endif
            
            struct node * root = malloc(sizeof(struct node));
            root->value = temp;
            if (hashtable[target] != NULL)
                root->next = hashtable[target];
            hashtable[target] = root;
            num += 1;
            index = 0;
            
            #ifdef EDBUG
            print_chain(hashtable[target]);
            #endif
        }
    }

    if (feof(file)){
        fclose(file);
        return true;
    }
    else{
        fclose(file);
        return false;
    }
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return num;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
 
void unload_chain(struct node *root)
{
    if (root->next != NULL)
        unload_chain(root->next);

    free(root->value);
    free(root);
}
 
bool unload(void)
{
    for(int i = 0; i < SIZE; i++)
    {
        if (hashtable[i] != NULL)
            unload_chain(hashtable[i]);
    }
    return true;
}

#ifdef DEBUG
int main (int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: speller dictionary\n");
        return 1;
    }
    
    char *dictionary = argv[1];
    
    print_hash();
    
    bool loaded = load(dictionary);
    // abort if dictionary not loaded
    if (!loaded)
    {
        printf("Could not load %s.\n", dictionary);
        return 2;
    }
    
    print_hash();
    unload();

}
#endif