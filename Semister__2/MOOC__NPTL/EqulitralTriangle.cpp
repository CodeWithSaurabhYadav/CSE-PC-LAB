#include<simplecpp>

main_program{
    turtleSim();

    int base = 100;
    int side = 10;

    repeat(24){
        repeat(4){
            forward(side*2);
            left(90);
        }
        repeat(3){
            forward(base);
            left(120);
        }
        repeat(3){
            forward(base*2);
            left(120);
        }
        left(15);
    }
    wait(20);
}
