#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - ........................
 * @head: ................................
 * @number: ..................................................
 * Return:.................................
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tem;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else if (number <= (*head)->n)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		tem = *head;
		while (tem->next != NULL && number > tem->next->n)
		{
			tem = tem->next;
		}
		new->n = number;
		new->next = tem->next;
		tem->next = new;
		return (new);
	}
	return (NULL);
}
