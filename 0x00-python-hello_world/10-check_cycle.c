#include "lists.h"

/**
* check_cycle - checks if a linked list contains a cycle
* @list: linked list to check
*
* Return: 1 if the list has a cycle, 0 if it doesn't
*/
int check_cycle(listint_t *list)
{
listint_t *temp;
listint_t **addr_list;
int i, j;

/* Allocating memory for the array that will store the addresses */
addr_list = malloc(sizeof(*addr_list));
if (!addr_list)
return (0);

i = 0;
temp = list;
while (temp != NULL)
{
/* Check if address is already in addr_list */
for (j = 0; j < i; j++)
{
if (addr_list[j] == temp)
{
free(addr_list);
return (1);
}
}

/* Add new address to addr_list */
addr_list[i] = temp;
i++;
addr_list = realloc(addr_list, (i + 1) * sizeof(*addr_list));
if (!addr_list)
return (0);
temp = temp->next;
}
free(addr_list);
return (0);
}
