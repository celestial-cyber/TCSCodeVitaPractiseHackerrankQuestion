import java.util.*;
public class Solution{

	public static void main(String args[]){
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		int low = input.nextInt();
		int high= input.nextInt();
		int sum = 0:
		int temp = num;

		while(temp!=0){

		int digit = temp%10;
		if(digits >=low && digit <=high){
			sum+=digit;
			}
			temp = temp/10;
			}
		System.out.print(sum);
}
}