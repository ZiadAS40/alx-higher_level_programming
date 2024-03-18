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
	int *buffer = malloc(sizeof(int) * buffer_size), *tmp_buffer;

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
			tmp_buffer = realloc(buffer, sizeof(int) * buffer_size);
			if (!tmp_buffer)
			{
				free(buffer);
				return (-1);
			}
			buffer = tmp_buffer;
		}
	}
	i--;
	while ((*head) != NULL)
	{
		if ((*head)->n != buffer[i])
		{
			free(buffer);
			return (0);
		}
		(*head) = (*head)->next;
		i--;
	}
	free(buffer);
	return (1);
}
