import java.util.Scanner;
public class Fibo{
  public static void main(String[] args){
   int n1 = 1;
   int n2 = 1;
   int sum = 0;
   Scanner onh = new Scanner(System.in);
   int n = onh.nextInt();
   for(int i=0;i<n;i++){
      
      n1=n2;
      n2=sum;
      sum = n1 + n2;
      
      
      continue;
    
    }
  
    System.out.println(sum);
  }
}