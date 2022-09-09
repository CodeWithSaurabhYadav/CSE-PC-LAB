class Parent{
    void show(){
        System.out.println("This is a parent class");
    }
}
class Child extends Parent{
    @Override
    void show(){
        System.out.println("This is overridden class");
    }
}
class Prog10{
    public static void main(String[] args) {
        Child obj = new Child();
        obj.show();
    }
}