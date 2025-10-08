# Define the order of elements as given in the problem
order = ['!', '#', '$', '%', '&', '*', '@', '^', '~']

# Map each character to its order index for easy sorting
order_index = {char: i for i, char in enumerate(order)}

# Read input
N = int(input())
nuts = input().split()
bolts = input().split()

# Sort nuts and bolts according to predefined order
nuts_sorted = sorted(nuts, key=lambda x: order_index[x])
bolts_sorted = sorted(bolts, key=lambda x: order_index[x])

# Output
print(' '.join(nuts_sorted))
print(' '.join(bolts_sorted))
