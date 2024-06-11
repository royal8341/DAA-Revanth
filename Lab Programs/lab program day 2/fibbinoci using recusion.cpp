#include<stdio.h>
int fibbi(int n)
{
	if (n<=1)
	return n;
	else
	return fibbi(n-1)+fibbi(n-2);
}
int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<=n;i++)
	{
		printf("%d",fibbi(i));
	}
  return 0;
}
