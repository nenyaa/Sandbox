a, b = map(int, input().split())

if a == 0:
    print("f(x)={}".format(b))
elif a == 1:
    if b < 0:
        print("f(x)=x{}".format(b))
    elif b > 0:
        print("f(x)=x+{}".format(b))
    else:
        print("f(x)=x")
elif a == -1:
    if b < 0:
        print("f(x)=-x{}".format(b))
    elif b > 0:
        print("f(x)=-x+{}".format(b))
    else:
        print("f(x)=-x")
else:
    if b < 0:
        print("f(x)={}x{}".format(a, b))
    elif b > 0:
        print("f(x)={}x+{}".format(a, b))
    else:
        print("f(x)={}x".format(a))
