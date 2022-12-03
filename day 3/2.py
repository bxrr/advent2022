def get_val(c):
    if ord(c) > ord('Z'):
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 27

sum = 0

with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    i = 0
    temp = []
    for l in lines:
        temp.append(set([*l]))
        i += 1

        if i == 3:
            i = 0
            result = temp[0].intersection(temp[1]).intersection(temp[2])
            sum += get_val(list(result)[0])
            temp = []
print(sum)