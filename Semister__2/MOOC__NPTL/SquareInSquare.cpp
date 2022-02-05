#include<simplecpp>
#include<cmath>

main_program{
    turtleSim();

    //calculations
    float P_side = 100;
    float S_side = sqrt((pow(P_side/2,2))*2);

    //Primary Square Formation
    repeat(4){
        forward(P_side);
        left(90);
    }

    //Changing the pen location
    penUp();forward(P_side/2);penDown();

    //Drawing the Secondary Square
    left(45);
    repeat(4){
        forward(S_side);
        left(90);
    }
    wait(20);
}
