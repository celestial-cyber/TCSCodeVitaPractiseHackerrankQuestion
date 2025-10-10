"""Given a number, in the form of an array Num[] of size N containing digits from 1 to 9(inclusive). The task is to find the next smallest palindrome strictly larger than the given number.

Input Format

First line: integer N — number of digits.

Second line: N space-separated integers — the digits of the number (each 0–9, usually 1–9 per problem).

Constraints

1 ≤ N ≤ 10^5 (practical limits depend on implementation)

0 ≤ Num[i] ≤ 9

The resulting palindrome may have N or N+1 digits (the all-9s case).

Output Format

Print the digits of the next smallest palindrome strictly larger than the given number, space-separated on a single line.

Sample Input 0

11
9 4 1 8 7 9 7 8 3 2 2
Sample Output 0

9 4 1 8 8 0 8 8 1 4 9
Sample Input 1

2
5 7
Sample Output 1

6 6
🔑 Key Idea

Mirror left to right:
Create a palindrome by copying the left half into the right half.

If this mirrored palindrome is strictly greater than the original → done.

If not, then we need to increment the middle (like addition with carry), then mirror again.

Special Case: If all digits are 9, then the answer is 100...001 (N+1 digits)."""

















