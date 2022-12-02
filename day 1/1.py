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

        print(max(cal))