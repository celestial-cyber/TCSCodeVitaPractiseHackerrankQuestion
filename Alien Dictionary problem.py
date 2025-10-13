"""Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language. Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Input Format

First line: two space-separated integers N and K.

Second line (or following tokens): N words (space-separated or newline-separated) — the dictionary in sorted order according to the alien language.

Constraints

1 ≤ N ≤ 10^4

1 ≤ K ≤ 26 (letters are 'a' through char('a'+K-1))

Each word contains only lowercase letters from the first K English letters.

Total length of all words is reasonable (implementation-dependent).

Output Format

A single integer: 1 if the order you returned is valid (reproduces the given sorted dictionary), otherwise 0.

Sample Input 0

5 4
baa abcd abca cab cada
Sample Output 0

1
Sample Input 1

5 5
edcba edccc dabce abcde edc"""


from collections import defaultdict, deque

def findOrder(words, n, k):
    # Step 1: Create adjacency list for graph of K characters
    adj = defaultdict(list)

    # Step 2: Build graph by comparing adjacent words
    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        # Find first different character
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                adj[w1[j]].append(w2[j])
                break

    # Step 3: Perform Topological Sort (Kahn’s Algorithm)
    indegree = {chr(ord('a') + i): 0 for i in range(k)}
    for u in adj:
        for v in adj[u]:
            indegree[v] += 1

    # Queue for characters with indegree 0
    q = deque([c for c in indegree if indegree[c] == 0])
    order = ""

    while q:
        ch = q.popleft()
        order += ch
        for neigh in adj[ch]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                q.append(neigh)

    # Step 4: Return order (may be shorter if not all letters appear)
    return order


# Main driver
n, k = map(int, input().split())
words = input().split()

# Step 5: Get the alien order
order = findOrder(words, n, k)

# Function to check if returned order is valid
def isValid(words, order):
    # Create rank mapping
    rank = {ch: i for i, ch in enumerate(order)}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if rank[w1[j]] > rank[w2[j]]:
                    return 0
                break
        else:
            if len(w1) > len(w2):
                return 0
    return 1

print(isValid(words, order))


