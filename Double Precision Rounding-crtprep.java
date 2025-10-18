import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double D = sc.nextDouble();
        int K = sc.nextInt();

        double rounded = Math.round(D * Math.pow(10, K)) / Math.pow(10, K);

        if (K == 0) {
            System.out.println((int)Math.round(D));
        } else {
            System.out.printf("%." + K + "f", rounded);
        }
    }
}
