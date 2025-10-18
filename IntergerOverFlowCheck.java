import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();
        long B = sc.nextLong();

        long product = A * B;

        long INT_MIN = -2147483648L;
        long INT_MAX = 2147483647L;

        if (product >= INT_MIN && product <= INT_MAX)
            System.out.println(product);
        else
            System.out.println(-1);
    }
}
