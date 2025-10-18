"""Given a double value D and an integer K, round D to K decimal places using the round- to-nearest rule (if the (K + 1)-th digit is ≥ 5, round up). Output the rounded value as an integer if K = 0, or as a double with exactly K decimal places otherwise.

Input Format

A double D and an integer K.

Constraints

−106 ≤ D ≤ 106, 0 ≤ K ≤ 6

Output Format

Output the rounded value as an integer if K = 0, or as a double with K decimal places.

Sample Input 0

3.14159 2
Sample Output 0

3.14
Sample Input 1

2.71828 0
Sample Output 1

3
Sample Input 2

-5.55555 1
Sample Output 2

-5.6"""

D, K = input().split()
D = float(D)
K = int(K)

rounded_value = round(D, K)

if K == 0:
    print(int(rounded_value))
else:
    # Ensure exactly K decimal places
    print(f"{rounded_value:.{K}f}")
