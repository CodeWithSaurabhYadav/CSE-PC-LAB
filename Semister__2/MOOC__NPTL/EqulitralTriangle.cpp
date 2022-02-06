#include<simplecpp>

main_program{
    turtleSim();

    int side = 100;
    repeat(4){
        forward(side);
        left(120);
    }
    wait(20);
}
