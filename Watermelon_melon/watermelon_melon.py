h = int(input())
k = int(input())

# بررسی اینکه آیا مجموع 2h + k زوج است
if (2 * h + k) % 2 == 0:
    # بررسی امکان تقسیم برابر در شرایط خاص
    if h == 0 and k % 2 != 0:
        print("NO")
    elif k == 0 and h % 2 != 0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
