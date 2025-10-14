import java.util.*;

public class Solution{
	public static void main(String args[]){
	Scanner input = new Scanner(System.in);

	int N = input.nextInt();
	int num = N;
	int sum = 0;

	while(num!==0){

	int digit = num%10;
	if(digit!=0 && digit%2==0 && N%digit ==0){

		sum+=digit;
	}

	System.out.print(sum);
}
}
}