//WAP to implement Linked list
import java.util.*;
public class issue17
{
    public class Node
    {
        int data;
        Node next;
        Node(int d)
        {
            data=d;
            next=null;
        }
    }
    public Node head=null;
    public Node tail=null;
    public void add(int d)
    {
        Node newnode=new Node(d);
        if(head==null)
        {
            head=newnode;
            tail=newnode;
        }
        else
        {
            tail.next=newnode;
            tail=newnode;
        }
    }
    public void display()
    {
        Node current=head;
        if(head==null)
        {
            System.out.println("List is empty");
        }
        else
        {
            while(current!=null)
            {
                System.out.print(current.data+" ");
                current=current.next;
            }
        }
    }
    public static void main(String args[])
    {
        issue17 obj=new issue17();
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of elements");
        int n=sc.nextInt();
        System.out.println("Enter the elements");
        for(int i=0;i<n;i++)
        {
            int d=sc.nextInt();
            obj.add(d);
        }
        System.out.println("The elements are");
        obj.display();
    }
    
}