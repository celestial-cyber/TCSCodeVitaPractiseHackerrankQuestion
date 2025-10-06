""" Given a number, in the form of an array Num[] of size N containing digits from 1 to 9(inclusive). The task is to find the next smallest palindrome strictly larger than the given number.

Input Format

The first line contains an integer N — the number of digits.

The second line contains N space-separated integers representing the digits of the number (Num[]).

Constraints

1 ≤ N ≤ 105

1 ≤ Num[i] ≤ 9 (digits are from 1 to 9, no leading zeros

Output Format

Print the digits of the next smallest palindrome strictly larger than the given number, separated by spaces.

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
Submissions: 345
Max Score: 20
Difficulty: Medium
Rate This Challenge:

    
More🔑 Key Idea

Mirror left half → right half

Make the number palindrome by copying the left side into the right.

If this palindrome is greater than the original, done.

If not greater:

Increment the middle (or left middle for even length) and handle carry.

Then mirror again.

✅ Step-by-Step Example

Input:

11
9 4 1 8 7 9 7 8 3 2 2


Original: 94187978322

Mirror left → 9418778149 (not bigger).

Increment middle → 94188088149.
✔ Answer: 94188088149."""
def next_palindrome(num):
    n, mid = len(num), len(num)//2
    i, j = mid-1, mid+(n%2)
    
    # Check if left half < right half
    while i >= 0 and num[i] == num[j]: i, j = i-1, j+1
    left_smaller = (i < 0 or num[i] < num[j])

    # Mirror left to right
    i, j = mid-1, mid+(n%2)
    while i >= 0: num[j], i, j = num[i], i-1, j+1

    if left_smaller:  # Need to increment middle
        carry, i = 1, mid-1
        if n % 2: num[mid], carry = (num[mid]+1)%10, (num[mid]+1)//10; j = mid+1
        else: j = mid
        while i >= 0 and carry:
            num[i], carry = (num[i]+1)%10, (num[i]+1)//10
            num[j], i, j = num[i], i-1, j+1
        if carry: return [1]+[0]*(n-1)+[1]
    return num

# Main
N = int(input())
Num = list(map(int, input().split()))
print(" ".join(map(str, next_palindrome(Num))))
