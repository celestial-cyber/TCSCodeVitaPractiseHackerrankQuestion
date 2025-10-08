"""Manipulations of arrays-crtprep
Problem
Submissions
Leaderboard
Discussions
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Input Format

The first line contains two space-separated integers, n (size of the array) and m (number of operations).

Each of the next m lines contains three space-separated integers a, b, and k.

Constraints

3 ≤ n ≤ 10^7

1 ≤ m ≤ 2 * 10^5

1 ≤ a ≤ b ≤ n

0 ≤ k ≤ 10^9

Output Format

Print a single integer, the maximum value in the array after all operations.

Sample Input 0

5 3
1 2 100
2 5 100
3 4 100
Sample Output 0

200
Sample Input 1

10 4
2 6 8
3 5 7
1 8 1
5 9 15
Sample Output 1

31
Submissions: 299
Max Score: 20
Difficulty: Medium
Rate This Challenge:

    
More
 
1
​"""

def arrayManipulation():
    n, m = map(int, input().split())
    arr = [0] * (n + 2)  # extra space for b+1

    for _ in range(m):
        a, b, k = map(int, input().split())
        arr[a] += k
        arr[b + 1] -= k

    max_val = 0
    current = 0
    for i in range(1, n + 1):
        current += arr[i]
        if current > max_val:
            max_val = current

    print(max_val)

arrayManipulation()
