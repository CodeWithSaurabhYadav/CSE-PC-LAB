#include<simplecpp>

main_program{

    int radius = 1;

    turtleSim();
    right(180);
    penUp();
    forward(100);
    penDown();
    right(180);

    //main loop
    repeat(6){
        repeat(480){
            forward(radius);
            right(1);
        }
        left(180);
    }

    //right()
    penUp();
    forward(100);
    left(90);
    forward(60);
    right(90);
    penDown();
    right(1);

    repeat(360){
        forward(radius);
        right(1);
    }

    wait(100);
}
