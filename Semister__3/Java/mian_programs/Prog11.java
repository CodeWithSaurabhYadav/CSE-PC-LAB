abstract class shape{
	abstract public void area();
	abstract public void display();
}

class circle extends shape{
	int radius;
	
	circle(){}
	circle(int r) { 
		radius=r;
	}
	public void area() { 
		System.out.println("The area of the circle is : " + 3.14*radius*radius); 
	}
	public void display() {
		System.out.println("The figure is Circle with radius : " + radius);
		area();
	}
}

class rectanglem extends shape{
	int length,breath;
	
	rectanglem(){}
	rectanglem(int l,int b) { 
		length=l;
		breath=b;
	}
	public void area() { 
		System.out.println("The area of the rectangle is : " + length*breath); 
	}
	public void display() {
		System.out.println("The figure is rectangle with length : " + length + " and breath : " + breath);
		area();
	}
}

class triangle extends shape{
	int base,height;
	
	triangle(){}
	triangle(int b,int h) { 
		base=b;
		height=h;
	}
	public void area() { 
		System.out.println("The area of the triangle is : " + 0.5*base*height); 
	}
	public void display() {
		System.out.println("The figure is triangle with base : " + base + " and height : " + height);
		area();
	}
}

public class Prog11 {
	
	public static void main(String args[])
	{
		shape s;
		triangle t = new triangle(1,3);
		rectanglem r = new rectanglem(3,4);
		circle c = new circle(10);
		
		s=t;
		s.display();
		s=r;
		s.display();
		s=c;
		s.display();
	}

}
