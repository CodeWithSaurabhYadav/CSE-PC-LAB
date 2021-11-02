#include<stdio.h>

void main()
{
	//Enrolment Number
	printf("-----------------\n");
	printf("|202103103510362|\n");
	printf("-----------------\n");

	//Program
	float cir_rad,cir_area;
	printf("________________________________________________\n");
	printf("\t\tArea Of Circle\n");	
	printf("________________________________________________\n");
	printf("Enter the radius of circle : ");
	scanf("%f",&cir_rad);
	cir_area=3.141*cir_rad*cir_rad;
	printf("Area of circle is : %f\n",cir_area);

	float rec_len,rec_bre,rec_area;
	printf("________________________________________________\n");
	printf("\t\tArea Of Rectancle\n");
	printf("________________________________________________\n");
	printf("Enter the length : ");
	scanf("%f",&rec_len);
	printf("Enter the breath : ");
	scanf("%f",&rec_bre);
	rec_area = rec_len*rec_bre;
	printf("Area of rectangle is : %f\n",rec_area);

	float squ_side,squ_area;
	printf("________________________________________________\n");
	printf("\t\tArea Of Square\n");	
	printf("________________________________________________\n");
	printf("Enter the side : ");
	scanf("%f",&squ_side);
	squ_area = squ_side*squ_side;
	printf("Area of square is : %f\n",squ_area);
}

