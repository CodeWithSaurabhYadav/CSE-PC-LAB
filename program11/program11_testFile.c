#include<stdio.h>
#include"enroll.h"

int main()
{
    //enrollment number
    enroll_print();
    /* code */
    int birth_date,birth_month,birth_year;
    int cur_date,cur_month,cur_year;
    printf("Enter current date : ");scanf("%d-%d-%d",&birth_date,&birth_month,&birth_year);
    printf("Enter Birth date : ");scanf("%d-%d-%d",&cur_date,&cur_month,&cur_year);
    //birth-year++ + CurrentYear--
    int value;
    value = 365*24*60*60*(birth_year-cur_year);
    //birth-year
    int birth_sec;
    birth_sec = (30-birth_date)*((12-birth_month)*30)*24*60*60;
    //current-year
    int cur_sec;
    cur_sec = (cur_date)*(30*cur_month)*24*60*60;
    //final Seconds lived (Approx...)
    int final_sec;
    final_sec = value + birth_sec + cur_sec;
    printf("You have lived %d seconds\n",final_sec);
}
