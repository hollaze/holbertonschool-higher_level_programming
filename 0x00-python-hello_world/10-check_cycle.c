#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int check_cycle(listint_t *list)
{
	listint_t *normal;
	listint_t *fast = fast->next;

	if (normal == NULL || fast == NULL)
		return (0);

	while (list != NULL)
	{
		normal = normal->next;
		fast = fast->next->next;

		if (normal == fast)
			return (1);
	}

return (0);
}
