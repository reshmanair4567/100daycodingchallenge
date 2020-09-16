fmt="%a %d %b %Y %H %M %S %z"
    for i in range(int(input())):
        print(int(abs((dt.striptime(),fmt)-(dt.striptime(),fmt)).total_seconds())