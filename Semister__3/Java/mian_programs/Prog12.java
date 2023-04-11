interface Class1{
    static void show(){
        System.out.println("I am first show method.");
    }
}
interface Class2{
    static void show(){
        System.out.println("I am second show method.");
    }
}
class ShowData implements Class1,Class2{

    public void show(){
        Class1.show();
        Class2.show();
        System.out.println("I am third show method");
    }
}
public class Prog12{
    public static void main(String[] args) {
        ShowData obj = new ShowData();
        obj.show();
    }
}