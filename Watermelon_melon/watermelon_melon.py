h = int(input())
k = int(input())

# Check if the sum of 2h + k is even
if (2 * h + k) % 2 == 0:
   # Investigating the possibility of equal division in certain circumstances
    if h == 0 and k % 2 != 0:
        print("NO")
    elif k == 0 and h % 2 != 0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
