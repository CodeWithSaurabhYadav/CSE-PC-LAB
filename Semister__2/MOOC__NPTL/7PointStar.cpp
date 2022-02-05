#include<simplecpp>

main_program{

    turtleSim();

    //calculation of point angles = 360/(point*2)

    repeat(7){
        forward(180);
        right(154.3);
    }

    right(180);
    penUp();
    forward(50);

    wait(10);
}
