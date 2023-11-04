#Generate the numbers which can be generated using the numbers which are provided.
##example:
IP: ```1,3,5```
OP:
```
combination= 7
1 
3 
1 3 
8 
1 8 
3 8 
1 3 8
```
##code java
```
import java.util.*;
public class Main {
  public static void main(String[]args){
    Scanner s=new Scanner(System.in);
    int n=s.nextInt();
    int sum=1;
    int a[]=new int[n];
    for(int i=0;i<n;a[i++]=s.nextInt());
    int combination=(1<<n)-1,start=1; //left shift give 2^n
    System.out.println("combination= "+combination);
    while(start<=combination){
     int index=0;
     int i=start;
     while(i!=0){
         if((i&1)==1)
         System.out.print(a[index]+" ");
         index++;
         i>>=1;
     }
     start++;
     System.out.println();
    }
  }
}
```
