// WAP To Print Right Angle Triangle Upto N Star's
import java.util.*;
public class issue3 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows");
        int n = sc.nextInt();
        int i, j;
        for (i = 1; i <= n; i++) 
        {
            for (j = 1; j <= i; j++) 
            {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
