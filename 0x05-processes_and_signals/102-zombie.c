#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>


/**
 * infinite_while - just an infinite loop
 *
 * Return: 0 if success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - creates 5 zombie processes
 */
void main(void)
{
	pid_t child;
	int i = 0;

	while (i < 5)
	{
		child = fork();
		while (child == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
}
