import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter the number of electricity units consumed: ");
        int units = input.nextInt();
        double bill = 0;

        if (units <= 100) {
            bill = units * 6;
        } else if (units <= 200) {
            bill = (100 * 6) + (units - 100) * 8;
        } else if (units <= 300) {
            bill = (100 * 6) + (100 * 8) + (units - 200) * 10;
        } else if (units <= 400) {
            bill = (100 * 6) + (100 * 8) + (100 * 10) + (units - 300) * 12;
        } else {
            bill = (100 * 6) + (100 * 8) + (100 * 10) + (100 * 12) + (units - 400) * 14;
        }

        System.out.println("Total Electricity Bill: ₹" + bill);

        input.close();
    }
}
