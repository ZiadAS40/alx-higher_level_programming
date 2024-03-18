#include "lists.h"
/**
 * is_palindrome - checks if it is a apalindrome.
 * @head: pointer to the first node.
 * Return: 1 if is
 * 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0;
	int buffer[1024];

	while (tmp != NULL)
	{
		buffer[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	i--;
	while ((*head) != NULL)
	{
		if ((*head)->n != buffer[i])
			return (0);
		(*head) = (*head)->next;
		i--;
	}
	return (1);
}
