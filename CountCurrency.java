import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter the amount to withdraw: ₹");
        int amount = input.nextInt();
        int originalAmount = amount;

        int[] notes = {2000, 500, 200, 100, 50, 20, 10, 5, 2, 1};
        int[] count = new int[notes.length];

        for (int i = 0; i < notes.length; i++) {
            if (amount >= notes[i]) {
                count[i] = amount / notes[i];   // Number of notes for this denomination
                amount = amount % notes[i];     // Remaining amount
            }
        }

        System.out.println("\nATM Denomination Breakdown for ₹" + originalAmount + ":");
        System.out.println("--------------------------------------------------");

        for (int i = 0; i < notes.length; i++) {
            System.out.println("₹" + notes[i] + " notes : " + count[i]);
        }

        input.close();
    }
}
