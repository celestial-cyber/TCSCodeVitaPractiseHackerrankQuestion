""" Minimum Insertions and Deletions to Make Arrays Identical-crtprepProblem
Submissions
Leaderboard
Discussions
Given two Arrays A[] and B[] of length N and M respectively. Find the minimum number of insertions and deletions on the array A[], required to make both the arrays identical. Note: Array B[] is sorted and all its elements are distinct, operations can be performed at any index not necessarily at end.

Input Format
The first line contains two integers N and M — the sizes of arrays A[] and B[].
The second line contains N space-separated integers representing array A[].
The third line contains M space-separated integers representing array B[].

Constraints
1 ≤ N, M ≤ 105
1 ≤ A[i], B[i] ≤ 105

Array B[] is sorted and contains distinct elements.
Output Format

Print a single integer — the minimum number of insertions and deletions required to make A[] identical to B[].
Sample Input 0

5 3
1 2 5 3 1
1 3 5
Sample Output 0
4
Sample Input 1
6 3
3 5 7 9 1 2
9 5 3
Sample Output 1
7
Submissions: 365
Max Score: 20
Difficulty: Medium
Rate This Challenge:

he operations needed = (N - LCS length) + (M - LCS length)

Where LCS = Longest Common Subsequence between A[] and B[].
Because:

Elements of A not in LCS must be deleted.

Elements of B not in LCS must be inserted.

Since B is sorted and distinct, we can speed things up by converting the problem into finding the Longest Increasing Subsequence (LIS) of A with respect to B.

Step-by-step solution:

Map each element of B to its index (since B is sorted and distinct).

Convert A into an array of indices, but only for elements that exist in B.

Example:

A = [1, 2, 5, 3, 1]
B = [1, 3, 5]
mapping = {1:0, 3:1, 5:2}
→ Transformed A = [0, 2, 1, 0]   (ignoring 2 since not in B)


Find the LIS of this transformed array.

This LIS length is exactly the LCS length of A and B.

(In example: LIS([0,2,1,0]) = [0,1] length = 2 → common subsequence = [1,3] or [1,5]).

Answer = (N - LCS) + (M - LCS).

Example 1
Input:
5 3
1 2 5 3 1
1 3 5

→ Transformed A = [0,2,1,0]
LIS length = 2
Answer = (5-2) + (3-2) = 3 + 1 = 4
✔ Output: 4

Example 2
Input:
6 3
3 5 7 9 1 2
9 5 3

→ mapping = {9:0, 5:1, 3:2}
→ Transformed A = [2,1,0]   (7,1,2 ignored)
LIS length = 1
Answer = (6-1) + (3-1) = 5 + 2 = 7
✔ Output: 7

    
"""

import bisect

def min_insert_delete(A, B):
    # Step 1: map elements of B to indices
    mapping = {val: i for i, val in enumerate(B)}

    # Step 2: transform A using mapping
    transformed = [mapping[x] for x in A if x in mapping]

    # Step 3: find LIS length in transformed
    lis = []
    for x in transformed:
        pos = bisect.bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x
    lcs_len = len(lis)

    # Step 4: compute result
    return (len(A) - lcs_len) + (len(B) - lcs_len)


# Driver
if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(min_insert_delete(A, B))
