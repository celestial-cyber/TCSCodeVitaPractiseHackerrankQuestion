import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter the amount to withdraw: ₹");
        int amt = input.nextInt();
        int originalAmt = amt;

        int r2000 = 0, r500 = 0, r200 = 0, r100 = 0, r50 = 0, r20 = 0, r10 = 0, r5 = 0, r2 = 0, r1 = 0;

        if (amt / 2000 > 0) {
            r2000 = amt / 2000;
            amt = amt % 2000;
        }
        if (amt / 500 > 0) {
            r500 = amt / 500;
            amt = amt % 500;
        }
        if (amt / 200 > 0) {
            r200 = amt / 200;
            amt = amt % 200;
        }
        if (amt / 100 > 0) {
            r100 = amt / 100;
            amt = amt % 100;
        }
        if (amt / 50 > 0) {
            r50 = amt / 50;
            amt = amt % 50;
        }
        if (amt / 20 > 0) {
            r20 = amt / 20;
            amt = amt % 20;
        }
        if (amt / 10 > 0) {
            r10 = amt / 10;
            amt = amt % 10;
        }
        if (amt / 5 > 0) {
            r5 = amt / 5;
            amt = amt % 5;
        }
        if (amt / 2 > 0) {
            r2 = amt / 2;
            amt = amt % 2;
        }
        if (amt / 1 > 0) {
            r1 = amt / 1;
            amt = amt % 1;
        }

        System.out.println("\nATM Denomination Breakdown for ₹" + originalAmt + ":");
        System.out.println("--------------------------------------------------");
        System.out.println("₹2000 notes : " + r2000);
        System.out.println("₹500 notes  : " + r500);
        System.out.println("₹200 notes  : " + r200);
        System.out.println("₹100 notes  : " + r100);
        System.out.println("₹50 notes   : " + r50);
        System.out.println("₹20 notes   : " + r20);
        System.out.println("₹10 notes   : " + r10);
        System.out.println("₹5 coins    : " + r5);
        System.out.println("₹2 coins    : " + r2);
        System.out.println("₹1 coins    : " + r1);

        input.close();
    }
}
