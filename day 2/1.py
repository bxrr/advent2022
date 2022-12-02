with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    key = {"A": "X", "B": "Y", "C": "Z"}
    skey = {"X": 1, "Y": 2, "Z": 3}

    score = 0
    
    for l in lines:
        if key[l[0]] == l[2]:
            score += 3
        elif l[0] == "A" and l[2] == "Y":
            score += 6
        elif l[0] == "B" and l[2] == "Z":
            score += 6
        elif l[0] == "C" and l[2] == "X":
            score += 6

        score += skey[l[2]]

print(score)