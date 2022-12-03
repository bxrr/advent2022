def get_val(c):
    if ord(c) > ord('Z'):
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 27

sum = 0

with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    for l in lines:
        first_half = set([*l[:len(l)//2]])
        second_half = set([*l[len(l)//2:]])
        sum += get_val(list(first_half.intersection(second_half))[0])

print(sum)