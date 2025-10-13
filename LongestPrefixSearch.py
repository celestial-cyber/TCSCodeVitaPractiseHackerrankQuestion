"""anf how tos solve this Longest Common Prefix-crtprep
Problem
Submissions
Leaderboard
Discussions
WAP to find Longest Common Prefix in an array of Strings Given an array of N strings, find the longest common prefix (LCP) shared by all strings. Print it in the format shown in the examples.

Input Format

First line: integer N — the number of strings.

Next line(s): N strings (space-separated or newline-separated).

Constraints

1 ≤ N ≤ 10^4

1 ≤ length of each string ≤ 10^3

Total number of characters across all strings ≤ 10^6 (practical bound)

Strings are case-sensitive and contain no whitespace (only standard visible characters).

Output Format

A single line:

Longest Prefix :

(where is the longest common prefix; if empty, print nothing after the colon)

Sample Input 0

4
javase javaee javaworld javabean
Sample Output 0

Longest Prefix : java
Sample Input 1

5
ball bat band building box
Sample Output 1

Longest Prefix : b
Submissions: 296
Max Score: 20
Difficulty: Medium
Rate This Challenge:

    
More"""


# Function to find the longest common prefix
def longestCommonPrefix(strs):
    # If list is empty
    if not strs:
        return ""

    # Start with the first string as prefix
    prefix = strs[0]

    # Compare prefix with each string
    for word in strs[1:]:
        # Reduce prefix until it matches the start of the word
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


# Main driver code
n = int(input().strip())
words = input().split() if n > 0 else []

result = longestCommonPrefix(words)
print(f"Longest Prefix : {result}")
























