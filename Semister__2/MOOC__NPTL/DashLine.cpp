#include<simplecpp>

main_program{
    turtleSim();

    penUp();
    repeat(4){
        repeat(5){
            penDown();
            forward(5);
            penUp();
            forward(5);
        }
        left(90);
    }
    wait(20);
}
