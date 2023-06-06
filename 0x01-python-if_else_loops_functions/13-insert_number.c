#include "lists.h"
#include <stdlib.h>

/**
* insert_node - Inserts a number into sorted singly linked list.
* @head: Double pointer to the first node of the linked list.
* @number: Integer to be included into the new node.
* Return: Address of new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t **current;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
current = head;

while (*current && ((*current)->n < number))
{
current = &(*current)->next;
}

new->next = *current;
*current = new;

return (new);
}
