with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    wkey = {"C": 1, "A": 2, "B": 3}
    lkey = {"B": 1, "C": 2, "A": 3}
    tkey = {"A": 1, "B": 2, "C": 3}
    skey = {"X": 0, "Y": 3, "Z": 6}

    score = 0
    
    for l in lines:
        if(l[2] == "X"):
            score += lkey[l[0]]
        elif(l[2] == "Y"):
            score += tkey[l[0]]
        elif(l[2] == "Z"):
            score += wkey[l[0]]

        score += skey[l[2]]

print(score)