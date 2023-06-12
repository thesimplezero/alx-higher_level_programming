#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next = NULL, *prev = NULL;

	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL, *rev = NULL, *mid = NULL;
	size_t size = 0, i = 0;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	tmp = *head;
	while (tmp != NULL)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < ((size / 2) - 1); i++)
	{
		tmp = tmp->next;
	}

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
	{
		return (0);
	}

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev != NULL)
	{
		if (tmp->n != rev->n)
		{
			return (0);
		}
		tmp = tmp->next;
		rev = rev->next;
	}

	reverse_listint(&mid);
	return (1);
}
