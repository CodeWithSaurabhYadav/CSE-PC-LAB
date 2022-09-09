import java.util.concurrent.locks.ReadWriteLock;

public class Parentclass {
    static int add(int a,int b){
        return (a+b);
    }
    static int sub(int a,int b){
        return (a-b);
    }
    static int mul(int a,int b){
        return (a*b);
    }
    static int div(int a,int b){
        if (b == 0){
            return 0;
        } else return (a/b);
    }
}
