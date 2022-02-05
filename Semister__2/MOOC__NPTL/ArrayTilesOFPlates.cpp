#include<simplecpp>

main_program{

    turtleSim();

    //Calculations

    cout << "Enter the number of patterns you want : ";
    int pattern_number;
    cin >> pattern_number;

    int num;
    num = 360/pattern_number;

    int angle_1 = 240;
    int angle_2 = 240 + num;
    repeat(pattern_number){
        forward(20);
        repeat(angle_1){
            forward(0.05);
            right(1);
        }
        forward(20);
        repeat(angle_2){
            forward(0.05);
            left(1);
        }
        }
    wait(200);
}
