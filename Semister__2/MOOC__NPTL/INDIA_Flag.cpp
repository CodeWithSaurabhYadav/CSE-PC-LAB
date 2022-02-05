 #include<simplecpp>

main_program{
    turtleSim();

    int length = 50;

    penUp();right(180);forward(200);penDown();

    right(90);
    forward(200);
    right(90);
    forward(400);
    right(90);
    forward(300);
    right(90);
    forward(400);
    right(90);
    forward(100);
    right(90);
    forward(400);

    penUp();left(90);forward(100);left(90);penDown();

    forward(400);
    left(90);

    penUp();forward(200);penDown();

    forward(400);
    left(-90);
    forward(20);
    left(-90);
    forward(700);
    left(-90);
    forward(20);

    penUp();
    forward(200);
    right(90);
    forward(150);
    left(90);
    penDown();

    repeat(24){
        repeat(3){
            forward(50);
            left(120);
        }
        left(15);
    }
    penUp();forward(500);
    wait(20);
}
