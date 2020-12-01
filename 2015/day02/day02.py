presents = []
with open('input.txt') as f:
    for box in f.readlines():
        present = [int(dim) for dim in box.strip().split('x')]
        presents.append(present)

def calc_paper(present: list):
    l, w, h = present
    side1 = l * w
    side2 = l * h
    side3 = h * w
    extra = min(side1, side2, side3)
    area = (2 * side1) + (2 * side2) + (2 * side3) + extra
    return area

def calc_ribbon(present: list):
    l, w, h = sorted(present)
    ribbon = (2 * l) + (2 * w)
    bow = l * w * h
    total = ribbon + bow
    return total

# for present in presents:
#     print(calc_paper(present))


print(calc_ribbon([2, 3, 4]))
print(calc_ribbon([4, 3, 2]))
print(calc_ribbon([1, 1, 10]))
# part 1
print(sum([calc_paper(present) for present in presents]))

#part 2
print(sum([calc_ribbon(present) for present in presents]))
