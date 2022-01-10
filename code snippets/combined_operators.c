#include<stdio.h>

void main()
{
    /* code */
    int num = 362;
    //arithmatic
    printf("%d\n",num+=2);
    printf("%d\n",num-=2);
    printf("%d\n",num*=2);
    printf("%d\n",num/=2);
    //bitwise
    printf("%d\n",num&=2);
    printf("%d\n",num|=2);
    printf("%d\n",num^=2);
    printf("%d\n",num>>=2);
    printf("%d\n",num<<=2);
}
