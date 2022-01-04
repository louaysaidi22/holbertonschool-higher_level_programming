#include "lists.h"
/**
 * insert_node - function in C that inserts a number
 * into a sorted singly linked list.
 * @head: head of linked list
 * @number: new node n
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new_node;
	int p;

	list = *head;
	p = list->n;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (list == NULL)
		*head = new_node;
	else if (p >= number)
	{
	new_node->next = list;
	*head = new_node;
	}
	else
	{
		while (list && list->next && p < number)
		{
			list = list->next;
			p = list->n;
		}
		new_node->next = list->next;
		list->next = new_node;
		}
	return (new_node);
}
