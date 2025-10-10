"""Given a positive integer N, swap (interchange) its first (most significant) and last (least significant) digits and print the resulting number. • If the number has fewer than two digits, print the message Interchange not possible. • Leading zeros produced by the swap are not preserved (i.e., the result is printed as a normal integer). Example: for 1257 → swap first 1 and last 7 → result 7251.

Input Format

A single line containing one integer: N

Constraints

• 1 ≤ N ≤ 2,147,483,647 (fits in a Java int) • N is a non-negative integer (the problem and reference implementation assume non-negative integers).

Output Format

• If N has fewer than 2 digits, print exactly: Interchange not possible. • Otherwise print the new integer after swapping the first and last digits:

Sample Input 0

1257
Sample Output 0

7251
Sample Input 1

8
Sample Output 1

Interchange not possible
Submissions: 162
Max Score: 20
Difficulty: Medium
Rate This Challenge:


### ✅ How it works

1. Convert the number to a string to access the digits easily.
2. If the length is less than 2 → print `"Interchange not possible"`.
3. Otherwise, construct a new string:

   * `num_str[-1]` → last digit
   * `num_str[1:-1]` → middle part
   * `num_str[0]` → first digit
4. Convert back to `int` to remove any leading zeros.

    """


# Read input
N = int(input().strip())

# Convert number to string to access digits
num_str = str(N)

# Check if the number has fewer than 2 digits
if len(num_str) < 2:
    print("Interchange not possible")
else:
    # Swap first and last digits
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]
    # Convert back to integer to remove any leading zeros
    result = int(swapped)
    print(result)


