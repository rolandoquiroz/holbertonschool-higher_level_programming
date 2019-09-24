#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: A singly-linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pnt1, *pnt2;

	if (list == NULL || list->next == NULL)
		return (0);
	pnt1 = list;
	pnt2 = pnt1->next;
	while (pnt1 != NULL && pnt2->next != NULL && pnt2->next->next != NULL)
	{
		if (pnt1 == pnt2)
			return (1);
		pnt1 = pnt1->next;
		pnt2 = pnt2->next->next;
	}
	return (0);
}
