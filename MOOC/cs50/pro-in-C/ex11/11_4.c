#include <stdio.h>

struct entry
{
    int value;
    struct entry *next;
};

void insertEntry(struct entry *to, struct entry *insert)
{
    insert->next = to->next;
    to->next = insert;
}

void printEntry(struct entry *list_pointer)
{
    list_pointer = list_pointer->next;
    while (list_pointer != (struct entry *)0){
        printf ("%i  ", list_pointer->value);
        list_pointer = list_pointer->next;
    }
    printf ("\n");
}
    
void removeEntry(struct entry *removedSec)
{
    removedSec->next = removedSec->next->next;
    
}

int main (void)
{
    struct entry n1, n2, n3, n4, start;
    struct entry *insert = &n4;
    
    start.next = &n1;
    
    n1.value = 100;
    n1.next = &n2;
    
    n2.value = 200;
    n2.next = &n3;
    
    n3.value = 300;
    n3.next = (struct entry *)0;
    
    n4.value = 50;
    n4.next = 0;
    
    printEntry(&start);
    insertEntry(&start, insert);
    printEntry(&start);
    removeEntry(&n4);
    printEntry(&start);
    removeEntry(&start);
    printEntry(&start);
    
    return 0;
}