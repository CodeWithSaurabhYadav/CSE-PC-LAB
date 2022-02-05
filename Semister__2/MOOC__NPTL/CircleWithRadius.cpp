#include<simplecpp>

main_program{

    //defining the radius

    float radius = 1;

    turtleSim();

    penUp();
    forward(radius);
    penDown();
    right(90);

    repeat(360){
        forward(radius);
        right(1);
    }

    wait(100);

}
