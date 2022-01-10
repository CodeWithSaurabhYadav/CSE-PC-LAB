#include<stdio.h>

int main()
{
    goto hello;
    printf("Hell");
    hello : 
        printf("hello world\n");
    return 0;
}
