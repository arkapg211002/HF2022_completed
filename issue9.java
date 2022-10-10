//WAP To Create Even & Odd List from given range N
import java.util.*;
public class issue9 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of N");
        int n=sc.nextInt();
        List<Integer> vals = new ArrayList<Integer>();
        System.out.println("The Empty List is: "+vals);
        for(int i=0;i<=n;i++)
        {
            vals.add(i);
        }
        System.out.println("The Full list is: "+vals);
        List<Integer>even=new ArrayList<>();
        List<Integer>odd=new ArrayList<>();
        for(int i=0;i<vals.size();i++)
        {
            if(i%2==0)
            {
                even.add(vals.get(i));
            }
            else
            {
                odd.add(vals.get(i));
            }
        }
        System.out.println("The Even List is: "+even);
        System.out.println("The Odd List is: "+odd);
    }
}
