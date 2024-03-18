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
	int i = 0, buffer_size = 128;
	int *buffer = malloc(sizeof(int) * buffer_size);

	if (!buffer)
		return (-1);
	while (tmp != NULL)
	{
		buffer[i] = tmp->n;
		tmp = tmp->next;
		i++;
		if (i >= buffer_size)
		{
			buffer_size += 128;
			buffer = realloc(buffer, sizeof(int) * buffer_size);
			if (!buffer)
				return (-1);
		}
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
