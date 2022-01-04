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

	list = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (list == NULL)
		*head = new_node;
	else if (list->n >= number)
	{
	new_node->next = list;
	*head = new_node;
	}
	else
	{
		while (list && list->next && list->next->n < number)
			list = list->next;
		new_node->next = list->next;
		list->next = new_node;
		}
	return (new_node);
}
