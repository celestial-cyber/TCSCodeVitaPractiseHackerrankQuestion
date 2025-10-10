"""Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. Find out the minimum possible difference of the height of shortest and longest towers after you have modified each tower.

You can find a slight modification of the problem here. Note: It is compulsory to increase or decrease (if possible) by K to each tower.

Input Format

The first line contains an integer K, the value by which tower heights can be increased or decreased.

The second line contains an integer N, the number of towers.

The third line contains N space-separated integers representing the array arr[] (the tower heights).

Constraints

1 ≤ N ≤ 10^5

1 ≤ K ≤ 10^4

0 ≤ arr[i] ≤ 10^9

Output Format

Print a single integer — the minimum possible difference between the maximum and minimum tower heights after modification.

Sample Input 0

2
4
1 5 8 10
Sample Output 0

5
Sample Input 1

3
6
2 5 7 4 3 2
Sample Output 1

4



This is the classic “Minimize the Heights II” problem with a twist:

Each tower must be either increased or decreased by K exactly once (if possible).

Heights must stay non-negative.

Goal: minimize (max height - min height) after modification.

🔑 Approach

Sort the array → makes it easier to control min/max ranges.

Initial difference = arr[n-1] - arr[0] (before modification).

After modifying:

The smallest tower may become larger (arr[0] + K).

The tallest tower may become smaller (arr[n-1] - K).

But we must check carefully for middle towers: some reduced by K, some increased by K.

For each index i (0 ≤ i < n-1):

Consider cutting between i and i+1.

Left side (arr[0..i]) → increase by K.

Right side (arr[i+1..n-1]) → decrease by K.

Candidate max = max(arr[i] + K, arr[n-1] - K).

Candidate min = min(arr[0] + K, arr[i+1] - K) (must be non-negative).

Update answer = min(answer, candidate_max - candidate_min).

✅ Python Implementation """

def minimize_difference(k, arr):
    n = len(arr)
    arr.sort()
    
    # Initial difference (no modification)
    ans = arr[-1] - arr[0]

    # Extreme boundaries after modification
    small = arr[0] + k
    big = arr[-1] - k

    for i in range(n - 1):
        min_val = min(small, arr[i+1] - k)
        if min_val < 0:
            continue  # skip invalid case
        max_val = max(big, arr[i] + k)
        ans = min(ans, max_val - min_val)

    return ans


# Driver code
if __name__ == "__main__":
    k = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(minimize_difference(k, arr))





















