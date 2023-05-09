#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
/**
 * main - ................
 * Return: .............
 */
int main(void)
{
	int i;

	srand(time(0));
	i = rand() - RAND_MAX / 2;

	if (i > 0)
		printf("%i is positive\n", i);
	else if (i < 0)
		printf("%i is negative\n",i);
	else
		printf("%i is zero\n", i);

	return (0);
}
