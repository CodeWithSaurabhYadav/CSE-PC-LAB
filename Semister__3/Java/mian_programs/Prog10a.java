class Child extends Parent{
    @Override
    void show2(){
        System.out.println("This is overridden class of parent 2");
    }
}
class Prog10a{
    public static void main(String[] args) {
        Child obj = new Child();
        obj.show();
    }
}