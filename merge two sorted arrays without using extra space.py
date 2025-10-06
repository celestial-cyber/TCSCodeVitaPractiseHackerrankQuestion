Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.

Input Format

The first line contains two integers N and M — the sizes of the two arrays.

The second line contains N space-separated integers representing arr1[].

The third line contains M space-separated integers representing arr2[].

Constraints

1 ≤ N, M ≤ 105

-109 ≤ arr1[i], arr2[i] ≤ 109

Both arrays are initially sorted in non-decreasing order.

You must merge them without using extra space.

Output Format

Print the merged array of size N + M in non-decreasing order.

Sample Input 0

4 5
1 3 5 7
0 2 6 8 9
Sample Output 0

0 1 2 3 5 6 7 8 9
Sample Input 1

4 5
3 5 7 2
8 5 12 2 2
Sample Output 1

2 2 5 5 2 3 7 8 12
ChatGPT said:

Got it ✅.
The problem is merge two sorted arrays without using extra space.

Since both arrays are already sorted, the best approach is the Gap Method (like Shell Sort idea).
We keep comparing elements across arr1 and arr2 and swap them if they’re out of order, gradually reducing the "gap".

🔹 Algorithm (Gap Method)

Set gap = ceil((N+M)/2).

Compare elements that are gap apart, swap if needed.

First inside arr1.

Then across arr1 & arr2.

Then inside arr2.

Reduce gap = ceil(gap/2) until it becomes 1, then stop.

Finally, arr1 and arr2 together will be sorted.

🔹 Code (Python Implementation)
import math

def merge(arr1, arr2, n, m):
    total = n + m
    gap = math.ceil(total / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < total:
            # Left index in arr1
            if i < n:
                a = arr1
                ai = i
            else:
                a = arr2
                ai = i - n

            # Right index in arr2 or arr1
            if j < n:
                b = arr1
                bj = j
            else:
                b = arr2
                bj = j - n

            # Compare and swap
            if a[ai] > b[bj]:
                a[ai], b[bj] = b[bj], a[ai]

            i += 1
            j += 1

        if gap == 1:
            break
        gap = math.ceil(gap / 2)


# -------- Driver Code --------
if __name__ == "__main__":
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    merge(arr1, arr2, N, M)

    print(*arr1, *arr2)

🔹 Sample Run
Input:
4 5
1 3 5 7
0 2 6 8 9

Output:
0 1 2 3 5 6 7 8 9


👉 This works without extra space (only O(1) extra variables).
👉 Time complexity: O((N+M) log(N+M)).

Do you want me to also give you a C++ version of the same (since many competitive coding platforms prefer C++)?

You said:
can u make it short 
ChatGPT said:

Got it 👍 You want a short and simple version.
Here’s a compact Python solution using the gap method:

import math

def merge(arr1, arr2, n, m):
    gap = math.ceil((n+m)/2)
    while gap > 0:
        i, j = 0, gap
        while j < n+m:
            # get array & index for i
            a, ai = (arr1, i) if i < n else (arr2, i-n)
            # get array & index for j
            b, bj = (arr1, j) if j < n else (arr2, j-n)
            if a[ai] > b[bj]:
                a[ai], b[bj] = b[bj], a[ai]
            i += 1; j += 1
        gap = 0 if gap == 1 else math.ceil(gap/2)

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
merge(arr1, arr2, N, M)
print(*arr1, *arr2)
