#include "lists.h"

/**
 * check_cycle - checks if there is a loop on the linked list.
 * @list: the first node on the list.
 * Return: 1 if there is a loop
 * 0 if no
*/

int check_cycle(listint_t *list)
{
	int i = 0, j, array_size = 32;
	listint_t *temp = list;
	listint_t **arr = malloc(sizeof(listint_t *) * array_size);


	while (temp != NULL)
	{
		*(arr + i) = temp;
		temp = temp->next;
		for (j = 0; j <= i; j++)
		{
			if (*(arr + j) == temp)
			{
				free(arr);
				return (1);
			}
		}
		i++;
		if (i >= array_size)
		{
			array_size += 32;
			arr = realloc(arr, sizeof(listint_t *) * array_size);
			if (!arr)
			{
				free(arr);
				return (-1);
			}
		}
	}
	free(arr);
	return (0);
}
