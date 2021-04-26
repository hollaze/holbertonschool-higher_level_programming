#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int check_cycle(listint_t *list)
{
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast && list && fast->next)
	{
		list = list->next;
		fast = fast->next->next;

		if (list == fast)
			return (1);
	}

	return (0);
}
