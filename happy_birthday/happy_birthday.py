# Read the number of cuts
n = int(input())
# Read the angles of the cuts
angles = list(map(float, input().split()))

# Sort the angles
angles.sort()

# Initialize the maximum piece size
max_piece = 0.0

# Calculate the size of the pieces between consecutive angles
for i in range(1, n):
    max_piece = max(max_piece, angles[i] - angles[i - 1])

# Calculate the piece that is between the last angle and the first angle
# (i.e., the distance from 360 degrees to the last angle)
max_piece = max(max_piece, 360.0 - angles[-1] + angles[0])

# Calculate the percentage of the cake that Tohmasb has eaten
result = (max_piece / 360.0) * 100

# Print the result with 6 decimal places
print(f"{result:.6f}")
