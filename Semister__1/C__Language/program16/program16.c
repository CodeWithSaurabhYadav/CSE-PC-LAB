#include<stdio.h>
#include"enroll.h"
long factorial();

int main()
{
    //enroll
    enroll_print();

    /* code */
    long num;
    printf("Enter a number : ");
    scanf("%ld",&num);
    printf("The factorial of %ld is %ld\n",num,factorial(num));
    return 0;
}
//factorial function
long factorial(long x)
{
    long fact = 1;
    for (long i = 1; i <= x; i++)
    {
        fact = fact*i;
    }
    return fact;
}