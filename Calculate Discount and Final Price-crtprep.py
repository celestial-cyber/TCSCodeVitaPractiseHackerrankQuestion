"""ou are given the total amount of shopping. Based on the total amount, calculate the discount and the final price to be paid according to the following discount rules: Shopping Amount Discount ≤ 800 No discount

800 and ≤ 1500 10% 1500 and ≤ 2500 15% 2500 and ≤ 5000 20% 5000 30% Your task is to calculate the final price after applying the appropriate discount.

Input Format

A single line containing the total amount of shopping: totalCost where totalCost is a floating-point number representing the total shopping amount.

Constraints

• 0 ≤ totalCost ≤ 1,000,000 • The input amount will be a non-negative floating-point number. That is, when the total shopping amount is less than 800 and less than or equal to $1500, then there will be a 10% discount to apply, and so on.

Output Format

Print a single line showing the amount to be paid after applying the discount, rounded to two decimal places:

Sample Input 0

700
Sample Output 0

700.00
Sample Input 1

2000
Sample Output 1

1700.00
Sample Input 2

6000
Sample Output 2

4200.00
Submissions: 148
Max Score: 20
Difficulty: Medium
Rate This Challenge:

✅ How it works

Check the amount against the discount brackets.

Apply the corresponding discount.

Multiply totalCost by (1 - discount) to get the final price.

Use Python’s f-string formatting to round to 2 decimal places."""






# Read input
totalCost = float(input().strip())

# Determine discount rate
if totalCost <= 800:
    discount = 0
elif totalCost <= 1500:
    discount = 0.10
elif totalCost <= 2500:
    discount = 0.15
elif totalCost <= 5000:
    discount = 0.20
else:
    discount = 0.30

# Calculate final price
final_price = totalCost * (1 - discount)

# Print result rounded to 2 decimal places
print(f"{final_price:.2f}")
