Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k.

Input Format

The first line contains two integers n and k — the size of the array and the product limit.

The second line contains n space-separated integers representing the array a[].

Constraints

1 ≤ n ≤ 105

1 ≤ a[i] ≤ 1000

1 ≤ k ≤ 1015

Output Format

Print a single integer — the number of contiguous subarrays whose product is strictly less than k.

Sample Input 0

4 10
1 2 3 4
Sample Output 0

7
Sample Input 1

8 50
3 5 2 7 9 4 1 8
Sample Output 1

17
ChatGPT said:

Got it ✅. This is a classic sliding window / two-pointer problem because all array elements are positive.

We want to count contiguous subarrays with product < k.

🔹 Key Idea:

Keep a window [left, right] and track its product.

Expand right and multiply the product by a[right].

While the product ≥ k, move left forward and divide a[left] out.

For every position of right, the number of subarrays ending at right and having product < k is (right - left + 1).

🔹 Python Implementation
n, k = map(int, input().split())
a = list(map(int, input().split()))

prod = 1
left = 0
count = 0

for right in range(n):
    prod *= a[right]
    
    while left <= right and prod >= k:
        prod //= a[left]
        left += 1
    
    count += right - left + 1

print(count)

🔹 How It Works

Example 0:

Input:
4 10
1 2 3 4


Subarrays with product < 10: [1], [2], [3], [4], [1,2], [2,3], [1,2,3] → 7 subarrays. ✅

Example 1:

Input:
8 50
3 5 2 7 9 4 1 8


Count = 17 ✅

🔹 Complexity

Time: O(n) — each element is multiplied/divided at most once.

Space: O(1) extra space.

This is efficient and works for n ≤ 10^5 and k ≤ 10^15.
