#include<stdio.h>
#include"enroll.h"
long int fact();
int main()
{
    //enroll 
    enroll_print();
    /* code */
    int n;
    printf("Enter Integer : ");
    scanf("%d",&n);
    printf("Factorial of %d is : %ld\n",n,fact(n));
    return 0;
}
//facrtorial function
long int fact(int n)
{
    if (n>=1)
    {
        return n*fact(n-1);
    }
    else return 1;
}
