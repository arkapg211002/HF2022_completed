//WAP To Find Largest Of Three Numbers
import java.util.*;
public class issue10 {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the value of A");
        int a=sc.nextInt();
        System.out.println("Enter the value of B");
        int b=sc.nextInt();
        System.out.println("Enter the value of C");
        int c=sc.nextInt();
        if(a>b && a>c)
            System.out.println("A is the largest number");
        else if(b>a && b>c)
            System.out.println("B is the largest number");
        else
            System.out.println("C is the largest number");
    }
}
