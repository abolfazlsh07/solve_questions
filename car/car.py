# Read the number of test cases
t = int(input())

# Initialize an empty list to store the results for each test case
r = []

# Loop through each test case
for _ in range(t):
    # Read two integers n (number of horizontal streets) and m (number of vertical streets)
    n, m = map(int, input().split())
    
    # If n and m are equal, meaning the grid is square
    if n == m:
        # The minimum time is n+1 (or m+1, since they're the same)
        r.append(n + 1)
    else:
        # Decrease both n and m by 1 to account for the first intersection movement
        n -= 1
        m -= 1
        # The minimum time is the maximum of n and m plus 1, as the car on the longer path dictates the time
        r.append(max(n, m) + 1)
        
# Loop through the result list and print each result
for i in r:
    print(i)
