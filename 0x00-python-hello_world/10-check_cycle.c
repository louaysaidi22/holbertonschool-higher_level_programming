#include "lists.h"
/**
 * check_cycle - function in C that checks
 * if a singly linked list has a cycle in it.
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *check;

	head = list;
	check = list;
	while (head && check && check->next)
	{
	head = head->next;
	check = check->next->next;
	if (head == check)
		return (1);
	}
	return (0);
}
