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

struct node
{
    bool value;
    struct node *children[27];
};
typedef struct node Node;
Node *root;
int num = 0;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char* word)
{
    short int idx = 0;
    short int target;
    Node *temp = root;
    while (word[idx] != '\0'){
        if (word[idx] == '\''){
            target = 26;
        }
        else{
            target = tolower(word[idx]) - 'a';
        }
        if (temp->children[target] == NULL)
            return false;
        else
            temp = temp->children[target];
        idx++;
    }
    
    return temp->value;
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    FILE *file = fopen(dictionary, "r");
    char c;
    root = malloc(sizeof(struct node));
    Node *temp = root;
    while ( (c = fgetc(file)) != EOF)
    {
        if (c == '\n'){
            temp->value = true;
            temp = root;
            num += 1;
        }
        else if (c == '\''){
            if (temp->children[26] != NULL){
                temp = temp->children[26];
            }
            else{
                temp->children[26] = malloc(sizeof(Node));
                temp =  temp->children[26];
                temp-> value = false;
            }
        }
        else{
            short int target = tolower(c) - 'a';
            if (temp->children[target] != NULL){
                temp = temp->children[target];
            }
            else{
                temp->children[target] = malloc(sizeof(Node));
                temp =  temp->children[target];
                temp-> value = false;
            }
        }
    }
    fclose(file);
    if (c == EOF)
        return true;
    else
        return false;
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
void unload_node(Node *root)
{
    for(int i = 0; i < 27; i++)
    {
        if (root->children[i])
            unload_node(root->children[i]);
    }
    free(root);
}

bool unload(void)
{
    unload_node(root);
    return true;
}
