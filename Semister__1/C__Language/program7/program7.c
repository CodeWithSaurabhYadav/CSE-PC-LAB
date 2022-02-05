#include<stdio.h>
#include"enroll.h"
void main()
{
	//Enrolment Number
	enroll_print();

	//Program
	printf("------------------------------------------------------------------------------------------\n");
	printf(" Student Details \n");
	printf("------------------------------------------------------------------------------------------\n");

	//Variables
	char name[25],enroll_num[20],college_name[100],course_name[100];

	//name
	printf("Name :");
	scanf("%[^\n]s", name);

	//Enroll No.
	printf("Enrollment number : ");
	scanf("\n%[^\n]s",enroll_num);
	
	//College
	printf("College name : ");
	scanf("\n%[^\n]s",college_name);

	//Course
	printf("Course name : ");
	scanf("\n%[^\n]s",course_name);

	//printing values
	printf("---------------------------------------------------------------------------------------------------------------------------------------\n");
	printf("\nYou have entered:\n");
	printf("Name : %s\n",name);
	printf("Enrollment number : %s\n",enroll_num);
	printf("College name : %s\n",college_name);
	printf("Course name : %s\n",course_name);
	printf("----------------------------------------------------------------------------------------------------------------------------------------\n");

}
