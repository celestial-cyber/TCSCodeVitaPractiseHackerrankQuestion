"""Given two long integers A and B, compute their product. If the product fits within an int data type (i.e., within [−231, 231 − 1]), output the product as an int; otherwise, output -1.

Input Format

Two long integers A and B.

Constraints

−1012 ≤ A, B ≤ 1012

Output Format

Output the product as an int if it fits within int range; otherwise, output -1.

Sample Input 0

1000 2000
Sample Output 0

2000000
Sample Input 1

1000000 1000000
Sample Output 1

-1"""

A, B = map(int, input().split())
product = A * B

INT_MIN = -2**31
INT_MAX = 2**31 - 1

if INT_MIN <= product <= INT_MAX:
    print(product)
else:
    print(-1)
