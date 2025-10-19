/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a string:");
        String s = input.nextLine();

        int lowerVowels = 0, upperVowels = 0, lowerConsonants = 0, upperConsonants = 0;
        int digits = 0, spaces = 0, specialChars = 0;

        String lowerV = "", upperV = "", lowerC = "", upperC = "";
        String digitStr = "", spaceStr = "", specialStr = "";

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                    lowerVowels++;
                    lowerV += ch;
                } else {
                    lowerConsonants++;
                    lowerC += ch;
                }
            } else if (ch >= 'A' && ch <= 'Z') {
                if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
                    upperVowels++;
                    upperV += ch;
                } else {
                    upperConsonants++;
                    upperC += ch;
                }
            } else if (ch >= '0' && ch <= '9') {
                digits++;
                digitStr += ch;
            } else if (ch == ' ') {
                spaces++;
                spaceStr += ch;
            } else {
                specialChars++;
                specialStr += ch;
            }
        }

        // Print results
        System.out.println("Lowercase Vowels: " + lowerVowels + " -> " + lowerV);
        System.out.println("Uppercase Vowels: " + upperVowels + " -> " + upperV);
        System.out.println("Lowercase Consonants: " + lowerConsonants + " -> " + lowerC);
        System.out.println("Uppercase Consonants: " + upperConsonants + " -> " + upperC);
        System.out.println("Digits: " + digits + " -> " + digitStr);
        System.out.println("Spaces: " + spaces + " -> '" + spaceStr + "'");
        System.out.println("Special Characters: " + specialChars + " -> " + specialStr);

        input.close();
    }
}
