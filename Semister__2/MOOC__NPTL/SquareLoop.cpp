#include<simplecpp>

main_program{
    turtleSim();

    int side = 50;
    repeat(40){
        repeat(4){
            forward(side);
            left(90);
        }
        repeat(4){
            forward(side*2);
            left(90);
        }
        repeat(4){
            forward(side*3);
            left(90);
        }
        repeat(4){
            forward(side*4);
            left(90);
        }
        repeat(4){
            forward(side*5);
            left(90);
        }
        left(10);
    }
    wait(20);
}
