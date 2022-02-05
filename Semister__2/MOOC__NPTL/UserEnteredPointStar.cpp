#include<simplecpp>

main_program{

    cout << "Enter the number of points you want in the star : ";
    int point;
    cin >> point;

    float angle = 180-(360/(point*2));

    turtleSim();

    repeat(point){
        forward(200);
        right(angle);
    }
    right(180);
    penUp();
    forward(50);
    right(180);

    wait(10);

}
