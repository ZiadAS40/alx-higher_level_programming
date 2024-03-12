#include "lists.h"

/**
 * insert_node - insert a number in a sorted list
 * @head: pointer to pointer to the first node.
 * @number: the number that should be iserted.
 * Return: pointer to the first node if success
 * NULL if fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *curr = *head;

	while (temp != NULL)
	{
		temp = temp->next;
		if (number >= curr->n && number < temp->n)
		{
           temp = malloc(sizeof(listint_t));
		   if (!temp)
		   return (NULL);
		   temp->n = number;
		   temp->next = curr->next;
		   curr->next = temp;
		   return (*head);
		}
		curr = curr->next;
	}
		return (NULL);
}