with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    cal = []
    temp = []

    for l in lines:
        if l: 
            temp.append(int(l))
        else:
            cal.append(sum(temp))
            temp = []

    sum = 0
    for i in range(3):
        sum += max(cal)
        cal[cal.index(max(cal))] = 0

    print(sum)