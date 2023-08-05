time = list(map(int, input().split()))
minTime = min(time)
count = time.count(minTime)
if count == 1:
    print(f"TAK {time.index(minTime) + 1}")
else:
    print("NIE")
